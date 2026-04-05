
import requests


from opentelemetry import trace

from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter, BatchSpanProcessor

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

from opentelemetry.instrumentation.requests import RequestInstrumentator
   
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)


RequestInstrumentator.instrument()

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

def validate_card():
    print("validating card")

def charge_bank():
    print("charging bank")
    try:
        
        url = "http://127.0.0.1:5000/charge"
                
        resp = requests.get(url)
       
    except Exception as err:  
        print(err)

def main():
     print("Calling Charge Bank...")
     result = charge_bank()
     print("Done! Charge Completed.")
if __name__ == "__main__":
    main()
