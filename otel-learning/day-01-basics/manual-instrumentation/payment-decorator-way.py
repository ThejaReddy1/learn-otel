from opentelemetry import trace

from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

def configure_tracer():
    exporter = ConsoleSpanExporter()
    span_processor = SimpleSpanProcessor(exporter)

    provider = TracerProvider()  # root tracer object

    provider.add_span_processor(span_processor)

    trace.set_tracer_provider(provider)  # trace.get_tracer 

    return trace.get_tracer("payment.py", "0.1.0")   # the object returned is used to create the spans


tracer = configure_tracer() 

@tracer.start_as_current_span("Staring Payment") # decorator way of creating spans the block of code under this decorator will be our span.
def process_payment():
    print("processing payment")
    validate_card()
    charge_bank()

@tracer.start_as_current_span("Validating Card")
def validate_card():
    print("validating card")

@tracer.start_as_current_span("Charging Bank")
def charge_bank():
    print("charging bank")


if __name__ == "__main__":
    with tracer.start_as_current_span("Payment Service"):   # Context manager (Once the control comes out this block of code it is going to close out the span automatically)
        process_payment()
