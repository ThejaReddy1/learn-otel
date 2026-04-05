from gc import callbacks
import random
import time, os
import psutil
from flask import Flask, request

from opentelemetry.metrics import set_meter_provider, get_meter_provider, Observation

from opentelemetry.sdk.metrics.view import ExplicitBucketHistogramAggregation, View

from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader

from opentelemetry.sdk.metrics import MeterProvider

from opentelemetry.sdk.resources import Resource


def configure_meter():
    exporter = ConsoleMetricExporter()
    reader = PeriodicExportingMetricReader(exporter, export_interval_millis=5000)  # for every 5 sec collect metrics and gives it to exporter

    buckets = [0.0, 20, 30, 60, 100, 250, 2000]

    view = View(instrument_name="total_request_duration", aggregation=ExplicitBucketHistogramAggregation(boundaries=buckets))

    provider = MeterProvider(metric_readers=[reader], resource=Resource.create(), views=[view])  # Central Registry fro all metric instuments

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

# to find out latencies (histogram). how long it took to complete a request
total_request_duration = meter.create_histogram("total_request_duration", description="Request Duration", unit="ms")

@app.before_request
def before_request():
    request.start_time = time.time()
    concurrent_requests.add(1)

@app.after_request
def after_request(response):
    request_latency = (time.time() - request.start_time) * 100
    concurrent_requests.add(-1)
    total_request_duration.record(request_latency)
    return response


@app.get("/products")
def get_products():
    requests_counter.add(1, {"route": "/products", "method": request.method}) 
    time.sleep(random.uniform(0.05, 1.5)) # to test latency 
    return "Get All Products"

@app.get("/products/<int:id>")
def get_product(id):
    time.sleep(random.uniform(0.05, 1.5))
    requests_counter.add(1, {"route": "/products", "method": request.method})
    return "Getting product details"

@app.post("/products")
def create_product():
    time.sleep(random.uniform(0.05, 1.5))
    requests_counter.add(1, {"route": "/products", "method": request.method})
    return "Creating Products"

@app.patch("/products/<int:id>")
def update_products(id):
    time.sleep(random.uniform(0.05, 1.5))
    requests_counter.add(1, {"route": "/products", "method": request.method})
    return "Updating Product"

@app.delete("/products/<int:id>")
def delete_products(id):
    time.sleep(random.uniform(0.05, 1.5))
    requests_counter.add(1, {"route": "/products", "method": request.method})
    return "Deleting Product"

@app.get("/cart")
def get_cart():
    time.sleep(random.uniform(0.05, 1.5))
    requests_counter.add(1, {"route": "/cart", "method": request.method})
    return "Get Cart"

@app.patch("/cart/<int:id>")
def update_cart(id):
    time.sleep(random.uniform(0.05, 1.5))
    requests_counter.add(1, {"route": "/cart", "method": request.method})
    return "Update Cart"


if __name__ == "__main__":
    app.run()
