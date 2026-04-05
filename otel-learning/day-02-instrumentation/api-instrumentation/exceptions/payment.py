# Resource attributes provide an immutable set of attributes that represents the entity  producing the telemetry. Metadata of who is generating telemetry
import requests
from opentelemetry.sdk.resources import Resource

from opentelemetry import trace

from opentelemetry.propagate import inject

from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter, BatchSpanProcessor

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

def configure_tracer():
    exporter = ConsoleSpanExporter()
    # exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
    
    # span_processor = SimpleSpanProcessor(exporter)
    span_processor = BatchSpanProcessor(exporter)

    resource = Resource.create({
        "service.name": "payment_service",
        "service.version": "0.2.0"
    })

    provider = TracerProvider(resource=resource)

    provider.add_span_processor(span_processor)

    trace.set_tracer_provider(provider)  # trace.get_tracer 

    return trace.get_tracer("payment.py", "0.1.0")   

tracer = configure_tracer()

@tracer.start_as_current_span("Staring Payment") 
def process_payment():
    
    span = trace.get_current_span()

    span.set_attributes({
        "user": "john",
        "account_number": "7372349",
        "bank": "SBI"
    })
    print("processing payment")
    validate_card()
    charge_bank()

@tracer.start_as_current_span("Validating Card")
def validate_card():
    print("validating card")

@tracer.start_as_current_span("Charge Bank")
def charge_bank():
    print("charging bank")

    with tracer.start_as_current_span("Request to Charge API", kind=trace.SpanKind.CLIENT) as span:
        try:
            
            url = "http://127.0.0.1:5000/charge"
            span.set_attributes({
                "HTTP_METHOD": "GET",
                "HTTP_URL": url
            })

            headers = {}
            inject(headers)
            span.add_event("Sending Request")                      
            resp = requests.get(url, headers=headers)
            span.add_event("Reuest Sent", attributes={"url":url})
            span.set_attribute("HTTP_STATUS_CODE", resp.status_code)
       
        except Exception as err:  
            # span.add_event("exeception", attributes={"exception": str(err)})
            span.record_exception(err)  # OTel has a function to record exceptions

            # by default OpenTelemetry will automatically record the exceptions we don't need actually any add_event() or record_exception() methods. 
if __name__ == "__main__":
    with tracer.start_as_current_span("Payment Service"):  
        process_payment()
