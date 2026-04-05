# Day 1 - OpenTelemetry Basics

## Overview

Day 1 focuses on the foundations: creating spans manually and understanding the resource metadata attached to telemetry.

## Learning Outcomes

- Understand what a tracer, span, and span processor are
- Create nested spans manually
- Add service metadata with resource attributes

## Prerequisites

```powershell
py -m pip install -r ..\..\shared-resources\python\requirements.txt
```

## Modules

- [Manual Instrumentation](./manual-instrumentation/README.md)
- [Resource Attributes](./resource-attributes/README.md)

## Expected Output

- Console spans printed in JSON-like form
- Parent-child span relationships
- A resource block that includes service metadata

## Troubleshooting

- If `py` fails, use `python` or `python3`.
- If imports fail, reinstall the shared requirements.