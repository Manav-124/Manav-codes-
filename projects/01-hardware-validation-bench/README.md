# 01 — Automated Hardware Validation Bench

## Problem
Manual board validation can become inconsistent when measurements, limits and results are recorded by hand. This project demonstrates a small automated test bench that applies engineering limits and produces traceable reports.

## Current Demo
The included `SimulatedBench` produces representative DMM-style voltage readings for three common power rails. **These readings are simulated, not measurements from a physical DUT.**

| Test | Lower Limit | Upper Limit |
|---|---:|---:|
| 3.3 V rail | 3.20 V | 3.40 V |
| 5 V rail | 4.85 V | 5.15 V |
| 12 V rail | 11.70 V | 12.30 V |

## Flow

```text
DUT / Simulator
      |
      v
Measurement Adapter
      |
      v
Limit Validation ---> PASS / FAIL
      |
      v
Timestamped CSV Report
```

## Run

```bash
python3 validation_bench.py
```

## Hardware Upgrade Path

The simulation adapter is intentionally separated from the validation logic. A physical implementation can replace it with:

- DMM over USB/serial
- Programmable bench power supply
- Oscilloscope measurement API
- Custom UART test jig

The limit engine and reporting layer can remain unchanged.

## Next Engineering Iterations

- Current consumption validation
- Ripple/noise measurement
- UART loopback test
- Device serial-number capture
- Retry policy for unstable readings
- JSON and HTML reports
