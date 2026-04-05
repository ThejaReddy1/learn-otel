from flask import Flask

from opentelemetry.metrics import set_meter_provider, get_meter_provider

from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader

from opentelemetry.sdk.metrics import MeterProvider

from opentelemetry.sdk.resources import Resource


def configure_meter():
    exporter = ConsoleMetricExporter()
    reader = PeriodicExportingMetricReader(exporter, export_interval_millis=5000)  # for every 5 sec collect metrics and gives it to exporter

    provider = MeterProvider(metric_readers=[reader], resource=Resource.create())  # Central Registry fro all metric instuments

    set_meter_provider(provider) # making provider global

    return get_meter_provider().get_meter(name="shopping-app", version="0.1.2")

meter = configure_meter()

app = Flask(__name__)


products_requests = meter.create_counter("products_requests_total", description="Total number of requests processed by the application", unit="1") # Counter Metric

cart_requests = meter.create_counter("cart_requests_total", description="Total number of requests processed by the application", unit="1") # Counter Metric


@app.get("/products")
def get_products():
    products_requests.add(1)
    return "Get All Products"

@app.get("/products/<int:id>")
def get_product(id):
    products_requests.add(1)
    return "Getting product details"

@app.post("/products")
def create_product():
    products_requests.add(1)
    return "Creating Products"

@app.patch("/products/<int:id>")
def update_products(id):
    products_requests.add(1)
    return "Updating Product"

@app.delete("/products/<int:id>")
def delete_products(id):
    products_requests.add(1)
    return "Deleting Product"

@app.get("/cart")
def get_cart():
    cart_requests.add(1)
    return "Get Cart"

@app.patch("/cart/<int:id>")
def update_cart(id):
    cart_requests.add(1)
    return "Update Cart"


if __name__ == "__main__":
    app.run()
