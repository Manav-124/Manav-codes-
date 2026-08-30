"""Analyze production-test logs and rank recurring failure modes."""
from collections import Counter

def summarize(records):
    failures = [r["failure"] for r in records if r["status"] == "FAIL"]
    return Counter(failures).most_common()

if __name__ == "__main__":
    demo = [
        {"status":"FAIL","failure":"3V3_LOW"}, {"status":"PASS","failure":""},
        {"status":"FAIL","failure":"UART_TIMEOUT"}, {"status":"FAIL","failure":"3V3_LOW"},
    ]
    print("Failure ranking:")
    for fault, count in summarize(demo): print(f"{fault:16} {count}")
