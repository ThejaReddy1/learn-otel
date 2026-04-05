# Prometheus Exporter

## Overview

This example exposes metrics over HTTP so Prometheus or a browser can scrape them.

## Learning Outcomes

- Use the Prometheus metric reader
- Expose a `/metrics` endpoint

## Step-by-Step

1. Run the app:

   ```powershell
   py .\main.py
   ```

2. Generate traffic against the Flask routes.
3. Open `http://localhost:8000/metrics`.

## Expected Output

- Prometheus text format metrics
- Counters, gauges, and histograms for the example routes

## Troubleshooting

- If `http://localhost:8000/metrics` is empty, make sure the app is still running.