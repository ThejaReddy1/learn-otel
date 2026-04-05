# Day 0 - Foundations Before You Instrument Anything

## Overview

Day 0 is the orientation layer for this repository. Before creating spans, starting the Collector, or exporting telemetry, a beginner should understand what observability is, what OpenTelemetry is responsible for, and how OTCA-style concepts fit together.

## Why Day 0 Matters

Many beginners jump directly into traces, metrics, or the Collector and end up following commands without understanding the system behind them. Day 0 fixes that.

By the end of this day, you should be able to answer:

- What problem does observability solve?
- How are logs, metrics, and traces different?
- Where does OpenTelemetry fit in the observability stack?
- What does the Collector do?
- What ideas show up repeatedly in OTCA learning?

## Observability In Plain Language

Observability is the ability to understand what a system is doing from the signals it produces.

In practice, that means answering questions like:

- Why is this request slow?
- Which service is failing?
- Did latency increase after a deploy?
- Are errors isolated or system-wide?
- Can I explain what happened without guessing?

Observability is not just dashboards. It is a way to investigate unknown problems using telemetry.

## The Three Core Signals

### Logs

Logs are event records.

Use logs when you want discrete details such as:

- an exception message
- a user action
- a deployment event
- a business event like "payment failed"

Think: "Something happened."

### Metrics

Metrics are numeric measurements over time.

Use metrics when you want:

- request counts
- error rates
- CPU and memory trends
- latency percentiles

Think: "How much, how often, how fast?"

### Traces

Traces show the lifecycle of a request or operation across one or more services.

Use traces when you want:

- request flow across services
- timing by step
- parent-child execution relationships
- context during debugging

Think: "Where did the time go, and what happened along the way?"

## OpenTelemetry In Plain Language

OpenTelemetry is the open standard and tooling ecosystem used to generate, collect, process, and export telemetry.

It helps you:

- instrument applications
- create traces, metrics, and logs
- standardize telemetry pipelines
- export data to many backends

OpenTelemetry is not the backend where you analyze data. It is the layer that helps produce and move telemetry.

## The Mental Model

Here is the easiest way to think about OpenTelemetry:

1. Your application does work.
2. Instrumentation produces telemetry about that work.
3. Telemetry is enriched with metadata.
4. The Collector can receive and process it.
5. Exporters send it to an observability backend.
6. Engineers use that data to troubleshoot and improve systems.

## Key Terms You Should Know First

### Span

A span represents one unit of work.

Examples:

- "validate payment"
- "query database"
- "call shipping service"

### Trace

A trace is a group of related spans that represent one full request or workflow.

### Resource

A resource describes the entity producing telemetry.

Examples:

- service name
- service version
- environment
- host metadata

### Attributes

Attributes are key-value details attached to telemetry.

Examples:

- HTTP method
- route
- user region
- database name

### Context Propagation

Context propagation is how trace context moves between services so multiple spans become one connected trace.

### Exporter

An exporter sends telemetry out of the app or Collector.

Examples:

- OTLP exporter
- Prometheus exporter
- vendor-specific exporters

### Collector

The Collector is a separate service that can receive, process, and export telemetry.

It helps centralize telemetry pipelines and keeps application code cleaner.

## App Vs Collector Responsibilities

### Application Side

The app is usually responsible for:

- creating spans, metrics, and logs
- adding business and request context
- exporting to OTLP or another receiver

### Collector Side

The Collector is usually responsible for:

- receiving telemetry from many apps
- batching or processing data
- routing telemetry to one or more destinations
- reducing backend coupling

## OTCA-Oriented Understanding

If you are learning with OTCA in mind, Day 0 should make these idea groups feel clear:

- telemetry signals: logs, metrics, traces
- instrumentation basics: manual, library-based, auto-instrumentation
- resources and attributes
- context propagation
- Collector roles: receivers, processors, exporters, pipelines
- OTLP as a common transport format

You do not need to memorize everything now. You only need a clean mental model so the later hands-on examples make sense.

## Common Beginner Misunderstandings

### "OpenTelemetry is my monitoring tool"

Not exactly. OpenTelemetry produces and moves telemetry. A backend stores, queries, and visualizes it.

### "Logs, metrics, and traces do the same thing"

They overlap, but they answer different kinds of questions. Strong observability usually uses all three.

### "The Collector is mandatory for every example"

No. It is extremely useful, especially in real systems, but some learning examples can export directly to the console or a backend.

### "Tracing means only microservices"

No. Even a single process can benefit from spans because they reveal timing and structure inside one application.

## Readiness Checklist

You are ready for Day 1 if you can explain:

- the difference between a log, metric, and trace
- what a span is
- what a trace is
- what resource attributes represent
- why context propagation matters
- why a Collector is useful

## How To Use Day 0 With The Rest Of The Repo

- Start here once before Day 1
- Revisit it after Day 3 if the Collector still feels abstract
- Revisit it before Day 6 if you want a stronger OTCA mental model

## Next Step

Move to [Day 1 - Basics](../day-01-basics/README.md) when you are comfortable with the vocabulary and mental model above.