"""Model watchdog supervision of an embedded main loop."""
class Watchdog:
    def __init__(self, timeout_ticks=3): self.timeout, self.age, self.resets = timeout_ticks, 0, 0
    def tick(self):
        self.age += 1
        if self.age >= self.timeout:
            self.resets += 1; self.age = 0; return "RESET"
        return "OK"
    def kick(self): self.age = 0

if __name__ == "__main__":
    w = Watchdog()
    for tick in range(8):
        if tick in (1, 5): w.kick()
        print(tick, w.tick())
