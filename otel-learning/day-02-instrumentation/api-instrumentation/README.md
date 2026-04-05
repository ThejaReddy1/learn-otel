# API Instrumentation

## Overview

These examples build a trace story step by step: instrument a Flask server, connect two services, propagate context, record errors, and observe status-related behavior.

## Learning Outcomes

- Instrument server spans for Flask endpoints
- Understand disconnected versus connected traces
- Record request metadata and errors on spans

## Step-by-Step

1. Server setup:

   ```powershell
   py .\server-setup\charge.py
   ```

2. Distributed tracing:

   - Terminal 1:

     ```powershell
     py .\distributed-tracing\charge.py
     ```

   - Terminal 2:

     ```powershell
     py .\distributed-tracing\payment.py
     ```

3. Context propagation:

   - Terminal 1:

     ```powershell
     py .\context-propagation\charge.py
     ```

   - Terminal 2:

     ```powershell
     py .\context-propagation\payment.py
     ```

4. Error handling and status behavior:

   ```powershell
   py .\exceptions\charge.py
   py .\exceptions\payment.py
   py .\status-codes\charge.py
   py .\status-codes\payment.py
   ```

## Expected Output

- A server span for `/charge`
- Separate traces before propagation
- Shared trace IDs after propagation

## Troubleshooting

- Start the `charge.py` service before the `payment.py` client.
- If requests fail, confirm the server is listening on `127.0.0.1:5000`.