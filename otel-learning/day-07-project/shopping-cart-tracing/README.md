# Shopping Cart Tracing

## Overview

This mini project simulates a small order flow and exports spans through OTLP.

## Learning Outcomes

- Trace a business workflow instead of a tiny toy function
- Export traces to the Collector

## Step-by-Step

1. Start the Collector:

   ```powershell
   docker compose -f ..\..\..\shared-resources\collector\docker-compose.yaml up -d
   ```

2. Run the project:

   ```powershell
   py .\shopping_cart.py
   ```

3. Inspect the Collector logs to confirm receipt.

## Expected Output

- Spans for order creation, order validation, and inventory reservation

## Troubleshooting

- If export fails, confirm the endpoint is `http://localhost:4318/v1/traces`.