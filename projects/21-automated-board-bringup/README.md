# 21 — Automated Board Bring-Up Orchestrator

A higher-complexity hardware-validation project modeling the workflow used when powering and validating a new board revision for the first time.

## Validation Pipeline

```text
DUT Identity
    ↓
Power Rails → Input Current
    ↓
Clock → Reset
    ↓
UART Loopback
    ↓
Memory Test
    ↓
GPIO Walking-1
    ↓
Final Board Disposition
```

## Why it is useful

A board can boot while still containing marginal power, clock, memory or I/O problems. This project treats bring-up as a repeatable sequence instead of a collection of manual checks.

## Architecture

`BringUp` owns the validation sequence while `SimulatedFixture` implements hardware access. A physical fixture can implement the same interface using a DMM, programmable PSU, oscilloscope, USB-UART bridge or custom test jig.

## Current Checks

- DUT/revision identity
- 1.8 V, 3.3 V and 5 V rails
- Input-current limit
- System-clock tolerance
- Reset-line behavior
- UART loopback
- Memory integrity
- GPIO walking-1 verification

The included measurements are simulation/demo values, not claimed laboratory captures.
