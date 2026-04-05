from gc import callbacks
import time, os
import psutil
from flask import Flask, request

from opentelemetry.metrics import set_meter_provider, get_meter_provider, Observation

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


requests_counter = meter.create_counter("http_requests_total", description="Total number of requests processed by the application", unit="1") # Counter Metric


concurrent_requests = meter.create_up_down_counter("concurrent_requests", description="Total number of requests in progress", unit="1") 
# any request comes in it bump it up and once request completes bump it down.

process = psutil.Process(os.getpid())
def memory_usage_callback(options):
    mem_info = process.memory_info()

    observations = [Observation(mem_info.rss, {"type": "rss"}), Observation(mem_info.vms, {"type": "vms"})]
    return observations
# how much memory my application using
meter.create_observable_gauge("application_memory_usage", description="Memory usage of application", unit="By", callbacks=[memory_usage_callback])

@app.before_request
def before_request():
    concurrent_requests.add(1)

@app.after_request
def after_request(response):
    concurrent_requests.add(-1)
    return response


@app.get("/products")
def get_products():
    requests_counter.add(1, {"route": "/products", "method": request.method}) 
    time.sleep(10)  # to  test active requests
    return "Get All Products"

@app.get("/products/<int:id>")
def get_product(id):
    requests_counter.add(1, {"route": "/products", "method": request.method})
    return "Getting product details"

@app.post("/products")
def create_product():
    requests_counter.add(1, {"route": "/products", "method": request.method})
    return "Creating Products"

@app.patch("/products/<int:id>")
def update_products(id):
    requests_counter.add(1, {"route": "/products", "method": request.method})
    return "Updating Product"

@app.delete("/products/<int:id>")
def delete_products(id):
    requests_counter.add(1, {"route": "/products", "method": request.method})
    return "Deleting Product"

@app.get("/cart")
def get_cart():
    requests_counter.add(1, {"route": "/cart", "method": request.method})
    return "Get Cart"

@app.patch("/cart/<int:id>")
def update_cart(id):
    requests_counter.add(1, {"route": "/cart", "method": request.method})
    return "Update Cart"


if __name__ == "__main__":
    app.run()
