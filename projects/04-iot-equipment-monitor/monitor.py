"""IoT equipment-health monitor using simulated telemetry packets."""
from dataclasses import dataclass, asdict
import json
import random
import time


@dataclass
class Telemetry:
    temperature_c: float
    vibration_g: float
    supply_v: float


def acquire() -> Telemetry:
    return Telemetry(
        temperature_c=round(random.gauss(39.0, 2.0), 2),
        vibration_g=round(abs(random.gauss(0.12, 0.03)), 3),
        supply_v=round(random.gauss(12.0, 0.08), 2),
    )


def classify(t: Telemetry) -> str:
    if t.temperature_c >= 70 or t.vibration_g >= 0.60 or not 11.4 <= t.supply_v <= 12.6:
        return "FAULT"
    if t.temperature_c >= 55 or t.vibration_g >= 0.35:
        return "WARNING"
    return "HEALTHY"


def packet(t: Telemetry) -> str:
    data = asdict(t)
    data["health"] = classify(t)
    data["source"] = "simulation"
    return json.dumps(data)


if __name__ == "__main__":
    print("Equipment Monitor — simulation mode (Ctrl+C to stop)")
    try:
        while True:
            print(packet(acquire()))
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nMonitor stopped")
