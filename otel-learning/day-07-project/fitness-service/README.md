# Fitness Service Metrics

## Overview

This mini project models a slightly richer service with request counters, queue size tracking, and request duration metrics.

## Learning Outcomes

- Combine multiple metric instruments in one app
- Expose metrics in Prometheus format

## Step-by-Step

1. Run the app:

   ```powershell
   py .\fitness.py
   ```

2. Generate traffic against routes such as `/workouts`, `/meals`, and `/pics`.
3. Open `http://localhost:8000/metrics`.

## Expected Output

- Metrics for total HTTP requests
- Queue length changes when image-processing work is queued

## Troubleshooting

- If `/metrics` is unavailable, make sure the process is still running.