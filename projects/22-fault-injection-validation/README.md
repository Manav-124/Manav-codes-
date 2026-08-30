# 22 — Fault Injection & Diagnostic Coverage Framework

Validation framework that intentionally introduces controlled fault conditions and checks whether the diagnostic system identifies the correct failure mode.

## Injected Scenarios

- Nominal operation
- 3.3 V brownout
- 3.3 V overvoltage
- Thermal fault
- UART communication failure

## Concept

```text
Fault Scenario → DUT Model → Diagnostics → Observed Alarm
                                      ↓
Expected Alarm ----------------> Compare → PASS/FAIL
```

This demonstrates an important validation principle: testing only the normal path is insufficient. Diagnostic logic should also be challenged with known failures.

The current implementation is simulation-based and can later drive physical fault relays, programmable supplies or fixture controls.
