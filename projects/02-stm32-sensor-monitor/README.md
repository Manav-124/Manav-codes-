# 02 — STM32 Sensor Health Monitor

Embedded C reference firmware for monitoring sensor and supply conditions using a small health-state machine.

## Demonstrated Concepts

- ADC telemetry representation
- Threshold-based diagnostics
- `OK → WARNING → FAULT` system states
- Embedded C structures and enums
- UART-friendly telemetry formatting
- Separation of hardware acquisition from decision logic

## Target Hardware

Designed to be straightforward to port to an STM32 development board. Replace the demo telemetry in `main.c` with STM32 HAL ADC acquisition and send the formatted status over UART.

## Suggested Physical Setup

```text
Temperature Sensor ---> ADC ----\
                               STM32 ---> UART ---> PC Logger
Supply Monitor -------> ADC ----/
                                 |
                                 +----> Status LED / Alarm
```

## Validation Cases

1. Normal temperature and supply → `OK`
2. Elevated temperature → `WARNING`
3. Low/high supply voltage → `FAULT`
4. Critical temperature → `FAULT`

Demo values in the source are illustrative and are not presented as physical measurements.
