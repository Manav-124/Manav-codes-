# 06 — Embedded Safety Controller

Portable C++ reference logic for a multi-sensor embedded safety system.

## Inputs

- Flame level
- Temperature
- Obstacle distance

## Outputs

- Alarm
- Pump
- Motor enable

## State Machine

```text
             abnormal condition
 SAFE ------------------------------> CAUTION
  ^                                      |
  |                                      | critical flame/temp
  |                                      v
  +-------------------------------- EMERGENCY
               conditions cleared
```

The reference implementation separates **decision logic** from **output control**, making the core behavior easy to unit-test before connecting physical sensors and actuators.

## Hardware Adaptation

The logic can be integrated with Arduino or STM32 GPIO/ADC drivers. Physical deployment should additionally include sensor-failure detection, actuator feedback, watchdog handling, and appropriate electrical safety protections.
