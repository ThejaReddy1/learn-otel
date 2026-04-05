# Library Instrumentation

## Overview

This module uses the `requests` instrumentor so outbound HTTP calls create spans automatically.

## Learning Outcomes

- Understand the value of library instrumentors
- Compare manual spans with library-generated spans

## Step-by-Step

1. Start the charge service:

   ```powershell
   py .\charge.py
   ```

2. In another terminal, run the client:

   ```powershell
   py .\payment.py
   ```

## Expected Output

- A client-side span created for the outgoing HTTP request

## Troubleshooting

- If the client cannot connect, make sure `charge.py` is already running.