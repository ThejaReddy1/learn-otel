# Resource Attributes

## Overview

This example adds metadata about the service that emits telemetry, such as `service.name` and `service.version`.

## Learning Outcomes

- Understand what resource attributes represent
- Distinguish span attributes from resource attributes
- Inspect service metadata in exported telemetry

## Step-by-Step

1. Run the example:

   ```powershell
   py .\payment.py
   ```

2. Look for the `resource` section in the output.

## Expected Output

- Span output that includes a `resource.attributes` block
- Service metadata that stays consistent across spans

## Troubleshooting

- If the resource block is missing, confirm the tracer provider is created with a `Resource`.
- If the script calls `http://127.0.0.1:5000/charge`, start the related Flask service from Day 2 or comment that section while exploring resources only.