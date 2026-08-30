"""I2C address scan model with expected-device validation."""
EXPECTED = {0x3C: "OLED", 0x48: "ADC", 0x68: "IMU/RTC"}

def validate(found):
    return [{"address": hex(addr), "device": name, "present": addr in found} for addr,name in EXPECTED.items()]

if __name__ == "__main__":
    simulated_found = {0x3C, 0x48, 0x68}
    for device in validate(simulated_found): print(device)
