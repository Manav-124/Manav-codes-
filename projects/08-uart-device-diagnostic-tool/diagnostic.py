"""UART-style device diagnostic parser and health classifier."""
from dataclasses import dataclass

@dataclass
class DeviceStatus:
    voltage: float
    temperature: float
    errors: int

def parse_frame(frame: str) -> DeviceStatus:
    fields = dict(item.split("=") for item in frame.strip().split(","))
    return DeviceStatus(float(fields["V"]), float(fields["TEMP"]), int(fields["ERR"]))

def classify(s: DeviceStatus) -> str:
    if s.errors or not 4.75 <= s.voltage <= 5.25 or s.temperature >= 80:
        return "FAULT"
    if s.temperature >= 65:
        return "WARNING"
    return "HEALTHY"

if __name__ == "__main__":
    sample = parse_frame("V=5.02,TEMP=41.5,ERR=0")
    print(sample, classify(sample))
