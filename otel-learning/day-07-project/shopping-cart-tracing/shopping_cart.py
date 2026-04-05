from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor, BatchSpanProcessor
from opentelemetry.sdk.resources import Resource

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

def configure_tracer():
    # exporter = ConsoleSpanExporter()
    exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
    # span_processor = SimpleSpanProcessor(exporter)
    span_processor = BatchSpanProcessor(exporter)
    resources = Resource.create({
        "service.name": "Shopping Cart Service",
        "service.version": "0.2.0"
    })
    provider = TracerProvider(resource=resources)
    provider.add_span_processor(span_processor=span_processor)
    trace.set_tracer_provider(provider)
    return trace.get_tracer("shopping-cart", "0.2.0")

def create_order():
    with tracer.start_as_current_span("Create Order"):
        print("creating Order")
        validate_order()
        reserve_inventory()

def validate_order():
    with tracer.start_as_current_span("Validate Order"):
        print("Validating Users Order")

def reserve_inventory():
    with tracer.start_as_current_span("Reserver Order"):
        print("Reserving Inventory")

if __name__ == "__main__":
    tracer = configure_tracer()
    create_order()
