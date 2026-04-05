# Collector Files

## Overview

These files are the shared Collector setup for the repository.

## Files

- `docker-compose.yaml`
- `collector-config-minimal.yaml`
- `collector-config-debug.yaml`

## Step-by-Step

1. Start the Collector:

   ```powershell
   docker compose -f .\shared-resources\collector\docker-compose.yaml up -d
   ```

2. Inspect the logs:

   ```powershell
   docker logs otel-collector
   ```

3. Stop the Collector:

   ```powershell
   docker compose -f .\shared-resources\collector\docker-compose.yaml down
   ```