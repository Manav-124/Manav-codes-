# 05 — Signal & Fault Analyzer

A compact Python utility for turning raw measurement samples into useful signal-quality statistics.

## Calculated Metrics

- Minimum / maximum
- Mean
- RMS
- Standard deviation
- Peak-to-peak variation
- Noise threshold pass/fail

## Engineering Use Cases

This type of analysis can support power-rail stability checks, sensor validation, repeated measurements, and automated fault screening.

```bash
python3 analyzer.py
```

The built-in sample array is illustrative demo data, not a physical instrument capture. Real CSV or serial acquisition is planned as a later extension.
