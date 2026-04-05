# Day 2 - Instrumentation

## Overview

Day 2 expands from basic spans into practical instrumentation for APIs, libraries, logs, and metrics.

## Learning Outcomes

- Instrument Flask services and client calls
- Understand distributed tracing and context propagation
- Capture logs and metrics alongside traces
- Compare manual, library-based, and auto-instrumentation approaches

## Prerequisites

```powershell
py -m pip install -r ..\..\shared-resources\python\requirements.txt
py -m pip install -r ..\..\shared-resources\python\requirements-auto.txt
```

## Modules

- [API Instrumentation](./api-instrumentation/README.md)
- [Library Instrumentation](./library-instrumentation/README.md)
- [Auto-Instrumentation](./auto-instrumentation/README.md)
- [Metrics](./metrics/README.md)
- [Logging Basics](./logging-basics/README.md)

## Troubleshooting

- Run one service per terminal window for client/server examples.
- If port `5000` is busy, stop the existing Flask app before starting another example.