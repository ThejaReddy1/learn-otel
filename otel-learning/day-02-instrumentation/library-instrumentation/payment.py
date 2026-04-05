# Resource attributes provide an immutable set of attributes that represents the entity  producing the telemetry. Metadata of who is generating telemetry
import requests

from opentelemetry import trace

from opentelemetry.sdk.resources import Resource

from opentelemetry.instrumentation.requests import RequestsInstrumentor

from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter, BatchSpanProcessor

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

resources=Resource.create({
    "service.name": "Casher API",
    "service.version": "0.3.0"
})

trace.set_tracer_provider(TracerProvider(resource=resources))
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)

RequestsInstrumentor().instrument()

def charge_bank():
    print("charging bank")

    try:
            
        url = "http://127.0.0.1:5000/charge"
        resp = requests.get(url)
      
    except Exception as err:  
        print(err)
def main():
     print("Calling bank charger...")
     charge_bank()
     print("Done! Charging bak done...")   
if __name__ == "__main__":
    main()
