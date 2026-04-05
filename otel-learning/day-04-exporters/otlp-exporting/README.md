# OTLP Exporting

## Overview

This example sends telemetry to an OTLP endpoint instead of printing everything to the console.

## Learning Outcomes

- Understand OTLP HTTP export
- Point traces and logs at the Collector

## Step-by-Step

1. Start the Collector:

   ```powershell
   docker compose -f ..\..\..\shared-resources\collector\docker-compose.yaml up -d
   ```

2. Run the example:

   ```powershell
   py .\main.py
   ```

3. Inspect the Collector logs:

   ```powershell
   docker logs otel-collector
   ```

## Expected Output

- The Collector logs show traces and logs received through OTLP

## Troubleshooting

- If export errors mention connection refusal, the Collector is not running or the endpoint is wrong.