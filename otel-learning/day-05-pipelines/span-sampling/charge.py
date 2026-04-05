# Instumenting a flask app, instumenting an API
from flask import Flask, request

from opentelemetry.sdk.resources import Resource

from opentelemetry import trace, context

from opentelemetry.propagate import extract

from opentelemetry.sdk.trace.sampling import TraceIdRatioBased

from opentelemetry.sdk.trace import TracerProvider

from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter, BatchSpanProcessor

from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

def configure_tracer():
    exporter = ConsoleSpanExporter()
    # exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")

    span_processor = BatchSpanProcessor(exporter)

    resource = Resource.create({
        "service.name": "Charge service",
        "service.version": "0.4.0"
    })

    sampler = TraceIdRatioBased(0.1) # 1 out of 10 traces sampled

    provider = TracerProvider(resource=resource, sampler=sampler)

    provider.add_span_processor(span_processor)

    trace.set_tracer_provider(provider)  # trace.get_tracer 

    return trace.get_tracer("charge.py", "0.4.0")   

tracer = configure_tracer()

app = Flask(__name__)

@app.before_request
def before_request_func():
    token = context.attach(extract(request.headers)) # retrives current context and makes it active
    request.environ["context_token"] = token         # this line makes it available in our flas application when ever we wan tot finish our code and revert back to the previous context or previous span

@app.teardown_request
def teardown_request_function(err):
    token = request.environ.get("context_token", None)
    if token:
        context.detach(token)


@app.route("/charge")
@tracer.start_as_current_span("Charge Account", kind=trace.SpanKind.SERVER)
def charge():
    # adding Span Attributes
    span = trace.get_current_span()
    span.set_attributes({
        "HTTP_METHOD": request.method,
        "CLIENT_IP": request.remote_addr,
        "HTTP_PATH": request.path
    })
    span.add_event("User has insufficient Funds, only has $5")
    return "Charging Users Bank Account"

if __name__ == "__main__":

    app.run(debug=True)
