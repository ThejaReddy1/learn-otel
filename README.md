# OpenTelemetry Learning Repository

This repository is organized as a beginner-friendly, day-wise OpenTelemetry learning path for hands-on practice with traces, metrics, logs, the Collector, OTLP exporters, and OTCA-focused study material.

## Repository Layout

```text
/otel-learning
  /day-00-foundations
  /day-01-basics
  /day-02-instrumentation
  /day-03-collector
  /day-04-exporters
  /day-05-pipelines
  /day-06-otca
  /day-07-project
/shared-resources
/docs
```

## Quick Start

1. Install the shared Python dependencies:

   ```powershell
   py -m pip install -r .\shared-resources\python\requirements.txt
   ```

2. If you want auto-instrumentation, also install:

   ```powershell
   py -m pip install -r .\shared-resources\python\requirements-auto.txt
   ```

3. Start the Collector when a lesson asks for OTLP export:

   ```powershell
   docker compose -f .\shared-resources\collector\docker-compose.yaml up -d
   ```

4. Follow the learning path:

   - [Day 0](./otel-learning/day-00-foundations/README.md)
   - [Day 1](./otel-learning/day-01-basics/README.md)
   - [Day 2](./otel-learning/day-02-instrumentation/README.md)
   - [Day 3](./otel-learning/day-03-collector/README.md)
   - [Day 4](./otel-learning/day-04-exporters/README.md)
   - [Day 5](./otel-learning/day-05-pipelines/README.md)
   - [Day 6](./otel-learning/day-06-otca/README.md)
   - [Day 7](./otel-learning/day-07-project/README.md)

## Troubleshooting

- If `py` is not available, use `python` or `python3`.
- If OTLP exports fail, make sure the Collector is running on `localhost:4317` and `localhost:4318`.
- If metrics are not visible in Prometheus format, keep the app running and check `http://localhost:8000/metrics`.

## Community

- Contribution guide: [CONTRIBUTING.md](./CONTRIBUTING.md)
- Shareable content: [docs](./docs/README.md)
- Reusable setup files: [shared-resources](./shared-resources/README.md)

## Sharing This Repo

If you want to publish your learning journey alongside the repository, start here:

- [Community sharing plan](./docs/community-sharing-plan.md)
- [Publishing workflow](./docs/publishing-workflow.md)
- [Post template](./docs/post-template.md)