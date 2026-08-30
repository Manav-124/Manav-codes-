"""Message protocol for a network-connected hardware test fixture."""
import json

def request(serial, tests):
    return json.dumps({"type":"run_test","serial":serial,"tests":tests})

def response(serial, results):
    passed = all(item["status"] == "PASS" for item in results)
    return json.dumps({"type":"test_result","serial":serial,"overall":"PASS" if passed else "FAIL","results":results})

if __name__ == "__main__":
    print(request("DEMO-0042", ["power","uart","gpio"]))
