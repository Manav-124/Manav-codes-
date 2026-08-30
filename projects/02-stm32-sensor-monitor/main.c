/*
 * STM32 Sensor Health Monitor - portable reference firmware
 *
 * Demonstrates ADC-style sensor validation and a fault-state machine.
 * Hardware-specific HAL calls can be connected in STM32CubeIDE.
 */
#include <stdint.h>
#include <stdio.h>

typedef enum {
    SYSTEM_OK,
    SYSTEM_WARNING,
    SYSTEM_FAULT
} system_state_t;

typedef struct {
    float temperature_c;
    float supply_v;
    uint16_t sensor_raw;
} telemetry_t;

static system_state_t evaluate_health(const telemetry_t *t)
{
    if (t->supply_v < 3.0f || t->supply_v > 3.6f || t->temperature_c > 85.0f)
        return SYSTEM_FAULT;

    if (t->temperature_c > 70.0f || t->supply_v < 3.15f)
        return SYSTEM_WARNING;

    return SYSTEM_OK;
}

static const char *state_name(system_state_t state)
{
    switch (state) {
        case SYSTEM_OK: return "OK";
        case SYSTEM_WARNING: return "WARNING";
        case SYSTEM_FAULT: return "FAULT";
        default: return "UNKNOWN";
    }
}

int main(void)
{
    /* Demo telemetry. Replace with ADC/HAL acquisition on target hardware. */
    telemetry_t sample = { 42.5f, 3.29f, 2174U };
    system_state_t state = evaluate_health(&sample);

    printf("temp=%.1fC supply=%.2fV adc=%u state=%s\n",
           sample.temperature_c,
           sample.supply_v,
           sample.sensor_raw,
           state_name(state));

    return (state == SYSTEM_FAULT) ? 1 : 0;
}
