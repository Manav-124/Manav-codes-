"""CAN-bus health logic using abstract frames; hardware adapter can be added later."""
from collections import Counter

def health(frames):
    ids = Counter(f["id"] for f in frames)
    errors = sum(bool(f.get("error")) for f in frames)
    return {"frames": len(frames), "unique_ids": len(ids), "errors": errors, "status": "PASS" if errors == 0 else "CHECK"}

if __name__ == "__main__":
    simulated = [{"id":0x101,"data":"01FF"},{"id":0x201,"data":"0A10"},{"id":0x101,"data":"01FE"}]
    print(health(simulated))
