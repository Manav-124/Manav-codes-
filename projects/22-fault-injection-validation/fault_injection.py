"""Fault-injection framework for validating diagnostic coverage."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Fault:
    name: str
    rail_v: float = 3.3
    temp_c: float = 40.0
    uart_ok: bool = True

FAULTS = [
    Fault("nominal"),
    Fault("3v3_brownout", rail_v=2.95),
    Fault("3v3_overvoltage", rail_v=3.65),
    Fault("thermal_fault", temp_c=92.0),
    Fault("uart_open", uart_ok=False),
]

def diagnostic(f):
    alarms=[]
    if not 3.1 <= f.rail_v <= 3.5: alarms.append("POWER_FAULT")
    if f.temp_c >= 85: alarms.append("THERMAL_FAULT")
    if not f.uart_ok: alarms.append("COMMS_FAULT")
    return alarms or ["NONE"]

def expected(f):
    mapping={"nominal":["NONE"],"3v3_brownout":["POWER_FAULT"],"3v3_overvoltage":["POWER_FAULT"],"thermal_fault":["THERMAL_FAULT"],"uart_open":["COMMS_FAULT"]}
    return mapping[f.name]

if __name__ == "__main__":
    passed=0
    for fault in FAULTS:
        observed=diagnostic(fault); ok=observed==expected(fault); passed+=ok
        print(f"{fault.name:18} expected={expected(fault)} observed={observed} {'PASS' if ok else 'FAIL'}")
    print(f"Diagnostic coverage: {passed}/{len(FAULTS)} scenarios")
