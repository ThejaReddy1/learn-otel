# Metrics

## Overview

These examples move from simple counters to async gauges, up-down counters, histograms, and cumulative metrics.

## Learning Outcomes

- Create core metric instruments
- Understand attributes, concurrency, and latency measurement

## Examples

- `counter-basics\main.py`
- `counter-basics\fitness_service.py`
- `async-gauge\main.py`
- `up-down-counter\main.py`
- `histogram\main.py`
- `cumulative-metrics\main.py`

## Step-by-Step

```powershell
py .\counter-basics\main.py
py .\async-gauge\main.py
py .\up-down-counter\main.py
py .\histogram\main.py
py .\cumulative-metrics\main.py
```

## Expected Output

- Periodic metric exports every few seconds
- Request counts grouped by route and method
- Histogram buckets for request duration

## Troubleshooting

- If the app starts but no metrics appear, wait for the export interval.
- If `psutil` import fails, reinstall the shared requirements.