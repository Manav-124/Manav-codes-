# Engineering Notes

## Validation Method

Every automated test in this repository follows four basic rules:

1. Define the expected operating range before evaluating the measurement.
2. Keep measurement acquisition separate from pass/fail logic.
3. Record enough context to reproduce and investigate a failure.
4. Never represent simulated values as physical measurements.

## Failure Investigation Pattern

```text
Failure detected
      |
      v
Confirm repeatability
      |
      v
Check power / connections / setup
      |
      v
Isolate failing subsystem
      |
      v
Compare expected vs observed signal
      |
      v
Identify probable root cause
      |
      v
Correct -> Retest -> Document
```

## Real Hardware Integration

The Python projects use adapter-style boundaries so simulated sources can later be replaced with serial, USB, VISA, or network-connected instruments. The embedded examples similarly keep application logic separate from MCU-specific HAL code.

This makes it possible to test the software logic on a computer first and then add physical hardware incrementally.
