"""Automated hardware validation bench.

Runs a repeatable power-rail validation sequence. The default adapter simulates
bench measurements so the project can be demonstrated without instruments.
Replace SimulatedBench with a real serial/VISA adapter for physical hardware.
"""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import csv
import random
from pathlib import Path


@dataclass
class TestResult:
    test: str
    measured: float
    unit: str
    minimum: float
    maximum: float
    status: str


class SimulatedBench:
    """Deterministic-enough stand-in for a DMM/power-supply test bench."""

    nominal = {"3V3": 3.30, "5V": 5.00, "12V": 12.00}

    def measure_voltage(self, rail: str) -> float:
        target = self.nominal[rail]
        return round(random.gauss(target, target * 0.006), 3)


LIMITS = {
    "3V3": (3.20, 3.40),
    "5V": (4.85, 5.15),
    "12V": (11.70, 12.30),
}


def validate_rail(bench: SimulatedBench, rail: str) -> TestResult:
    low, high = LIMITS[rail]
    measured = bench.measure_voltage(rail)
    return TestResult(
        test=f"{rail} power rail",
        measured=measured,
        unit="V",
        minimum=low,
        maximum=high,
        status="PASS" if low <= measured <= high else "FAIL",
    )


def run_validation() -> list[TestResult]:
    bench = SimulatedBench()
    return [validate_rail(bench, rail) for rail in LIMITS]


def save_report(results: list[TestResult]) -> Path:
    reports = Path(__file__).parent / "reports"
    reports.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = reports / f"validation_{stamp}.csv"
    with path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=asdict(results[0]).keys())
        writer.writeheader()
        writer.writerows(asdict(result) for result in results)
    return path


if __name__ == "__main__":
    results = run_validation()
    print("\nAUTOMATED HARDWARE VALIDATION")
    print("-" * 52)
    for result in results:
        print(f"{result.test:20} {result.measured:>7.3f} {result.unit}  {result.status}")
    overall = "PASS" if all(r.status == "PASS" for r in results) else "FAIL"
    print("-" * 52)
    print(f"Overall result: {overall}")
    print(f"Report: {save_report(results)}")
