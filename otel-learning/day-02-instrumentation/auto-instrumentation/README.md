# Auto-Instrumentation

## Overview

This example runs a Flask app with OpenTelemetry auto-instrumentation so you can capture telemetry without changing the application code.

## Learning Outcomes

- Understand when auto-instrumentation is useful
- Bootstrap instrumentation libraries for a Python app

## Step-by-Step

1. Install instrumentors:

   ```powershell
   opentelemetry-bootstrap -a install
   ```

2. Start the app:

   ```powershell
   opentelemetry-instrument --traces_exporter console --metrics_exporter console --service_name products py .\products.py
   ```

3. Send a request to `http://127.0.0.1:5000/`.

## Expected Output

- A trace for `GET /`
- Console-exported telemetry without manual tracer setup inside the app

## Troubleshooting

- If `opentelemetry-instrument` is not recognized, reopen the terminal after installing the packages.