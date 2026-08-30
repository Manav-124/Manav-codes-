"""Production test station prototype with unit traceability."""
from dataclasses import dataclass
from datetime import datetime, timezone
import sqlite3
import random
from pathlib import Path

DB = Path(__file__).parent / "test_history.db"


@dataclass
class Check:
    name: str
    value: float
    low: float
    high: float
    unit: str

    @property
    def passed(self) -> bool:
        return self.low <= self.value <= self.high


def simulated_checks() -> list[Check]:
    """Representative simulated station measurements."""
    return [
        Check("input_current", round(random.gauss(0.42, 0.015), 3), 0.35, 0.50, "A"),
        Check("logic_rail", round(random.gauss(3.30, 0.02), 3), 3.20, 3.40, "V"),
        Check("output_rail", round(random.gauss(5.00, 0.03), 3), 4.85, 5.15, "V"),
    ]


def initialize(conn: sqlite3.Connection) -> None:
    conn.execute("""CREATE TABLE IF NOT EXISTS results (
        timestamp TEXT, serial TEXT, test TEXT, value REAL,
        unit TEXT, low REAL, high REAL, status TEXT
    )""")


def run_unit(serial: str) -> bool:
    checks = simulated_checks()
    with sqlite3.connect(DB) as conn:
        initialize(conn)
        timestamp = datetime.now(timezone.utc).isoformat()
        for check in checks:
            status = "PASS" if check.passed else "FAIL"
            conn.execute(
                "INSERT INTO results VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (timestamp, serial, check.name, check.value, check.unit,
                 check.low, check.high, status),
            )
            print(f"{check.name:18} {check.value:>7} {check.unit}  {status}")
    return all(c.passed for c in checks)


if __name__ == "__main__":
    serial = input("Unit serial number: ").strip() or "DEMO-0001"
    print(f"\nTesting {serial} [SIMULATION MODE]\n")
    passed = run_unit(serial)
    print(f"\nFINAL: {'PASS' if passed else 'FAIL'}")
