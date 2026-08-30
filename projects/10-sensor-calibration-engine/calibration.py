"""Two-point sensor calibration utility."""
from dataclasses import dataclass

@dataclass
class Calibration:
    slope: float
    offset: float
    def apply(self, raw: float) -> float:
        return self.slope * raw + self.offset

def two_point(raw1, ref1, raw2, ref2):
    if raw1 == raw2:
        raise ValueError("calibration points must differ")
    slope = (ref2-ref1)/(raw2-raw1)
    return Calibration(slope, ref1-slope*raw1)

if __name__ == "__main__":
    cal = two_point(102, 0.0, 912, 100.0)
    print(f"Calibrated reading: {cal.apply(510):.2f}")
