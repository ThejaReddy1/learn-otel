from flask import Flask, request
from opentelemetry.metrics import set_meter_provider, get_meter_provider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader
from opentelemetry.sdk.metrics.view import ExplicitBucketHistogramAggregation, View
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from prometheus_client import start_http_server
import threading
import time
import random

def configure_meter():
    start_http_server(8000)
    # exporter = ConsoleMetricExporter()
    # reader = PeriodicExportingMetricReader(exporter, export_interval_millis=5000)
    reader = PrometheusMetricReader()
    buckets = [0.0, 20, 30, 60, 100, 250, 500, 1000]
    view = View(
        instrument_name="total_request_duration",
        aggregation=ExplicitBucketHistogramAggregation(boundaries=buckets)
    )
    provider = MeterProvider(resource=Resource.create(), metric_readers=[reader])
    set_meter_provider(provider)
    return get_meter_provider().get_meter(name="shopping-app", version="0.1.2")

meter = configure_meter()

http_total_requests = meter.create_counter("http_requests_total", unit="1", description="Total number of requests processed")

queue_length = meter.create_up_down_counter("queue_length", unit="1", description="Number of image processing tasks in queue")

# Add your histogram metric here
total_request_duration = meter.create_histogram("total_requet_duration", unit="ms", description="Duration of each HTTP request in milliseconds")

app = Flask(__name__)

task_queue = []

def process_image_task(task_id):
    processing_time = 10
    print(f"[Task {task_id}] Processing for {processing_time} seconds...")
    time.sleep(processing_time)
    queue_length.add(-1, {"route": "/pics"})
    print(f"[Task {task_id}] Done processing.")


@app.before_request
def before_request():
    request.start_time = time.time()
    simulated_delay = random.uniform(0.01, 1.0)
    time.sleep(simulated_delay)

@app.after_request
def after_request(response):
    request_latency = (time.time() - request.start_time) * 1000
    total_request_duration.record(request_latency)
    return response

@app.post("/pics")
def upload_pic():
    http_total_requests.add(1, {"route": "/pics", "method": request.method})
    task_id = len(task_queue) + 1
    task_queue.append(task_id)
    queue_length.add(1, {"route": "/pics"})
    thread = threading.Thread(target=process_image_task, args=(task_id,))
    thread.start()
    return f"Image {task_id} uploaded and queued for processing."

@app.get("/workouts")
def get_products():
    http_total_requests.add(1, {"route": "/workouts", "method": request.method})
    return "Get All workouts"

@app.post("/workouts")
def create_products():
    http_total_requests.add(1, {"route": "/workouts", "method": request.method})
    return "Create Workout"

@app.delete("/workouts")
def delete_products():
    http_total_requests.add(1, {"route": "/workouts", "method": request.method})
    return "Delete Workout"

@app.get("/meals")
def get_meals():
    http_total_requests.add(1, {"route": "/meals", "method": request.method})
    return "Get All Meals"

@app.post("/meals")
def create_meals():
    http_total_requests.add(1, {"route": "/meals", "method": request.method})
    return "Create Meal"

@app.delete("/meals")
def delete_meals():
    http_total_requests.add(1, {"route": "/meals", "method": request.method})
    return "Delete Meal"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
