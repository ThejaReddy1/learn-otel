# Manual Instrumentation

## Overview

These examples show the smallest useful tracing setup: a tracer provider, a span processor, a console exporter, and a few spans.

## Learning Outcomes

- Create spans with context managers
- Create spans with decorators
- Recognize parent and child span relationships

## Step-by-Step

1. Run the basic example:

   ```powershell
   py .\payment.py
   ```

2. Run the decorator-based example:

   ```powershell
   py .\payment-decorator-way.py
   ```

3. Compare the span names and nesting in the console output.

## Expected Output

- A top-level span for the payment service
- Child spans for validation and bank charging

## Troubleshooting

- If there is no output, confirm the script exits normally.
- If you want OTLP export instead of console output, move to Day 4.