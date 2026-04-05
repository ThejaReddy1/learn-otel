# Day 4 - Exporters and Backends

## Overview

Day 4 focuses on how telemetry leaves your app: OTLP for traces and logs, and Prometheus for metrics scraping.

## Learning Outcomes

- Export traces and logs with OTLP
- Correlate logs with traces
- Expose metrics for Prometheus scraping

## Modules

- [OTLP Exporting](./otlp-exporting/README.md)
- [Trace-Log Correlation](./trace-log-correlation/README.md)
- [Prometheus Exporter](./prometheus-exporter/README.md)

## Troubleshooting

- Start the Collector before running OTLP examples.
- For Prometheus output, keep the app running while you visit `http://localhost:8000/metrics`.