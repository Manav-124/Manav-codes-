"""Multi-rail power supervisor with tolerance and fault reporting."""
RAILS = {"1V8": (1.8, .05), "3V3": (3.3, .04), "5V": (5.0, .03), "12V": (12.0, .03)}

def inspect(measurements):
    report = {}
    for rail, (nominal, tolerance) in RAILS.items():
        low, high = nominal*(1-tolerance), nominal*(1+tolerance)
        value = measurements[rail]
        report[rail] = {"value": value, "limits": (round(low,3), round(high,3)), "status": "PASS" if low <= value <= high else "FAIL"}
    return report

if __name__ == "__main__":
    for rail, result in inspect({"1V8":1.79,"3V3":3.31,"5V":4.98,"12V":12.08}).items():
        print(rail, result)
