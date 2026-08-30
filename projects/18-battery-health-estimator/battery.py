"""Simple battery state-of-charge and health screening utility."""
def estimate(voltage, loaded_voltage, nominal_capacity, measured_capacity):
    soc = max(0, min(100, (voltage - 3.2) / (4.2 - 3.2) * 100))
    soh = max(0, min(100, measured_capacity / nominal_capacity * 100))
    sag = voltage - loaded_voltage
    return {"soc_percent": round(soc,1), "soh_percent": round(soh,1), "load_sag_v": round(sag,3), "status": "CHECK" if sag > .35 or soh < 80 else "GOOD"}

if __name__ == "__main__": print(estimate(4.05, 3.88, 2500, 2320))
