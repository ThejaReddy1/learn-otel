# Using difffernt BathSpanProcessor and Differnt Exporter

from opentelemetry import trace

from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter, BatchSpanProcessor

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

def configure_tracer():
    # exporter = ConsoleSpanExporter()
    exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
    
    # span_processor = SimpleSpanProcessor(exporter)
    span_processor = BatchSpanProcessor(exporter)

    provider = TracerProvider()

    provider.add_span_processor(span_processor)

    trace.set_tracer_provider(provider)  # trace.get_tracer 

    return trace.get_tracer("payment.py", "0.1.0")   

tracer = configure_tracer()

@tracer.start_as_current_span("Staring Payment") 
def process_payment():
    print("processing payment")
    validate_card()
    charge_bank()

def validate_card():
    with tracer.start_as_current_span("Validating Card"):
        print("validating card")

def charge_bank():
    with tracer.start_as_current_span("Charging Bank"):
        print("charging bank")

if __name__ == "__main__":
    with tracer.start_as_current_span("Payment Service"):  
        process_payment()
