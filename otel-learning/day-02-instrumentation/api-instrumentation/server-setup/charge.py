# Instumenting a flask app, instumenting an API
from flask import Flask, request

from opentelemetry.sdk.resources import Resource

from opentelemetry import trace

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

    provider = TracerProvider(resource=resource)

    provider.add_span_processor(span_processor)

    trace.set_tracer_provider(provider)  # trace.get_tracer 

    return trace.get_tracer("charge.py", "0.4.0")   

tracer = configure_tracer()

app = Flask(__name__)


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
    return "Charging Users Bank Account"

if __name__ == "__main__":

    app.run(debug=True)
