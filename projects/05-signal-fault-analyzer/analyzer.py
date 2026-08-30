"""Small signal-quality analyzer using only the Python standard library."""
from dataclasses import dataclass
from statistics import mean, pstdev
import math


@dataclass
class SignalReport:
    samples: int
    minimum: float
    maximum: float
    average: float
    rms: float
    standard_deviation: float
    peak_to_peak: float


def analyze(values: list[float]) -> SignalReport:
    if not values:
        raise ValueError("at least one sample is required")
    avg = mean(values)
    return SignalReport(
        samples=len(values),
        minimum=min(values),
        maximum=max(values),
        average=avg,
        rms=math.sqrt(mean(v * v for v in values)),
        standard_deviation=pstdev(values),
        peak_to_peak=max(values) - min(values),
    )


def flag_noise(report: SignalReport, max_stddev: float) -> bool:
    return report.standard_deviation > max_stddev


if __name__ == "__main__":
    # Illustrative captured-style samples; not claimed as physical measurements.
    demo = [3.30, 3.31, 3.29, 3.30, 3.32, 3.28, 3.30, 3.31, 3.29, 3.30]
    report = analyze(demo)
    print(report)
    print("Noise check:", "FAIL" if flag_noise(report, 0.025) else "PASS")
