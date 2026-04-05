# Trace-Log Correlation

## Overview

This example shows why logs become more useful when they carry trace context.

## Learning Outcomes

- Run traces and logs together in one flow
- Understand how logs help explain what happened inside a trace

## Step-by-Step

1. Run the example:

   ```powershell
   py .\main.py
   ```

2. Review the sample output file:

   - [output.json](./output.json)

## Expected Output

- Logs emitted inside traced functions such as booking and searching
- Trace spans surrounding the same application flow

## Troubleshooting

- If you only see spans or only logs, verify that both providers are configured before the functions run.