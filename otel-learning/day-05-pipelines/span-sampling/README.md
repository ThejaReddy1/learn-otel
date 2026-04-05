# Span Sampling

## Overview

This module demonstrates ratio-based sampling on the server side.

## Learning Outcomes

- Understand why sampling exists
- Observe that not every request becomes a fully sampled trace

## Step-by-Step

1. Start the sampled server:

   ```powershell
   py .\charge.py
   ```

2. In another terminal, send requests with:

   ```powershell
   py .\payment.py
   ```

3. Repeat the client call several times and compare the output.

## Expected Output

- Some requests show sampled traces while others do not

## Troubleshooting

- Sampling does not guarantee a visible trace on every request.