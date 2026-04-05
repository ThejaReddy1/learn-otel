# Span Processors

## Overview

This example introduces `BatchSpanProcessor`, which batches spans before export and is closer to production behavior than immediate export.

## Learning Outcomes

- Understand the role of a span processor
- Compare `SimpleSpanProcessor` and `BatchSpanProcessor`

## Step-by-Step

1. Run the example:

   ```powershell
   py .\payment.py
   ```

2. Review the code and note the configured exporter.
3. If you want OTLP export, start the Collector and switch to the OTLP exporter path already shown in the sample.

## Expected Output

- Console spans by default
- Or OTLP-exported spans when the Collector-backed exporter is enabled

## Troubleshooting

- If nothing appears immediately, remember that batched export may wait briefly before flushing.