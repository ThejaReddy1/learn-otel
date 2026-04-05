# Day 5 - Advanced Pipelines and Processors

## Overview

Day 5 is about what happens between telemetry creation and backend storage: batching, sampling, and pipeline design.

## Learning Outcomes

- Explain what span processors do
- Understand why batching helps production systems
- Explore sampling tradeoffs

## Modules

- [Span Processors](./span-processors/README.md)
- [Span Sampling](./span-sampling/README.md)

## Troubleshooting

- If sampling seems random, that is expected; run the example multiple times.
- If you are comparing console output with OTLP output, make sure you know which exporter is currently enabled in the code.