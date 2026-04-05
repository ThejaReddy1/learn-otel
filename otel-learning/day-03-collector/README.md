# Day 3 - Collector Deep Dive

## Overview

Day 3 introduces the OpenTelemetry Collector as the central place to receive, process, and export telemetry.

## Learning Outcomes

- Start the Collector with Docker
- Understand receivers, processors, exporters, and pipelines

## Step-by-Step

1. Start the Collector:

   ```powershell
   docker compose -f ..\..\shared-resources\collector\docker-compose.yaml up -d
   ```

2. Review the shared config:

   - [Collector README](../../shared-resources/collector/README.md)
   - [Minimal config](../../shared-resources/collector/collector-config-minimal.yaml)
   - [Debug config](../../shared-resources/collector/collector-config-debug.yaml)

3. Re-run an OTLP example from Day 4 or Day 7.

## Expected Output

- A running `otel-collector` container
- Telemetry accepted on `4317` and `4318`

## Troubleshooting

- If the container does not start, make sure Docker Desktop is running.
- Inspect the logs with `docker logs otel-collector`.