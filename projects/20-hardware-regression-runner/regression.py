"""Regression runner comparing current hardware-test results with a baseline."""
def compare(baseline, current, tolerance=0.05):
    report = []
    for test, expected in baseline.items():
        actual = current[test]
        delta = actual - expected
        limit = abs(expected) * tolerance
        report.append({"test":test,"baseline":expected,"current":actual,"delta":round(delta,4),"status":"PASS" if abs(delta) <= limit else "REGRESSION"})
    return report

if __name__ == "__main__":
    baseline={"3v3":3.30,"current":0.42,"temp":41.0}
    current={"3v3":3.31,"current":0.43,"temp":42.2}
    for result in compare(baseline,current): print(result)
