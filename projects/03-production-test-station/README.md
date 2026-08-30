# 03 — Production Test Station

A Python prototype for a manufacturing/production test workflow where every unit is identified, tested against engineering limits, and recorded for traceability.

## Workflow

```text
Scan / Enter Serial
        |
        v
Electrical Tests
        |
        v
Apply Limits
    /       \
 PASS      FAIL
    \       /
     v     v
   SQLite History
```

## Features

- Unit serial-number tracking
- Multiple electrical checks
- Per-test pass/fail limits
- Overall unit disposition
- Timestamped SQLite test history
- Simulation mode for equipment-independent demonstration

## Run

```bash
python3 test_station.py
```

The current measurement source is explicitly simulated. A real station could connect the same workflow to programmable instruments or a custom fixture.

## Why This Matters

Production testing is not only about obtaining a measurement. A useful station must make the procedure repeatable, preserve traceability, enforce the correct limits, and make failures easy to investigate.
