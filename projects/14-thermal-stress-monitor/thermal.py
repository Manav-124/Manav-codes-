"""Thermal stress-cycle monitor for validation experiments."""
def analyze_cycle(samples, warning=70.0, critical=85.0):
    peak = max(samples)
    above_warning = sum(t >= warning for t in samples)
    return {"peak_c": peak, "warning_samples": above_warning, "status": "FAIL" if peak >= critical else "PASS"}

if __name__ == "__main__":
    simulated = [25, 31, 43, 58, 67, 72, 74, 68, 51, 35]
    print(analyze_cycle(simulated))
