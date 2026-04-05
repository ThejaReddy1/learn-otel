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

tracer = configure_tracer() # making tracer object global if it under if block or main block decorators fail

@tracer.start_as_current_span("Staring Payment") # decorator way of creating spans the block of code under this decorator will be our span.
def process_payment():
    # with tracer.start_as_current_span("Starting Payment"):
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
    # tracer = configure_tracer()

    # span = tracer.start_span("Starting Payment")      # manual way of starting and closing Spans
    with tracer.start_as_current_span("Payment Service"):   # Context manager (Once the control comes out this block of code it is going to close out the span automatically)
        process_payment()

    # print("end of block of code")
    # span.end()
