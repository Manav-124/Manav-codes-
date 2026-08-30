/* Embedded Safety Controller - portable Arduino/MCU-style reference logic */
#include <stdint.h>

enum class SafetyState { SAFE, CAUTION, EMERGENCY };

struct Inputs {
    int flame_level;
    float temperature_c;
    float distance_cm;
};

struct Outputs {
    bool alarm;
    bool pump;
    bool motors_enabled;
};

SafetyState evaluate(const Inputs& in) {
    if (in.flame_level >= 4 || in.temperature_c >= 80.0f)
        return SafetyState::EMERGENCY;
    if (in.flame_level > 0 || in.temperature_c >= 60.0f || in.distance_cm < 20.0f)
        return SafetyState::CAUTION;
    return SafetyState::SAFE;
}

Outputs control(SafetyState state) {
    switch (state) {
        case SafetyState::EMERGENCY:
            return {true, true, false};
        case SafetyState::CAUTION:
            return {true, false, false};
        case SafetyState::SAFE:
        default:
            return {false, false, true};
    }
}

int main() {
    Inputs demo{0, 31.0f, 75.0f};
    Outputs out = control(evaluate(demo));
    return (out.alarm || out.pump) ? 1 : 0;
}
