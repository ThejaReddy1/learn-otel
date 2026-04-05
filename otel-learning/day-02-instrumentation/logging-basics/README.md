# Logging Basics

## Overview

This example shows how Python logging can be routed through OpenTelemetry logging components.

## Learning Outcomes

- Create an OpenTelemetry logger provider
- Send standard Python logs through an OTel logging handler

## Step-by-Step

```powershell
py .\main.py
```

## Expected Output

- Log messages for booking, searching, and reservation events
- Console output produced through the OpenTelemetry log exporter

## Troubleshooting

- If you only see standard log lines, check that `LoggingHandler` is wired into `logging.basicConfig(...)`.