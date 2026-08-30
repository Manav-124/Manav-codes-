# 04 — IoT Equipment Monitor

A lightweight telemetry monitor that models equipment-health data moving from an embedded device into a monitoring system.

## Telemetry

- Temperature
- Vibration
- Supply voltage
- Calculated health state

Packets are encoded as JSON, making the output easy to publish through MQTT or send to an API later.

## Architecture

```text
Sensors -> MCU/Edge Device -> JSON Telemetry -> MQTT/API -> Dashboard
                                  |
                                  +-> Health Classification
```

## Run

```bash
python3 monitor.py
```

The included source uses simulated telemetry and marks every packet with `"source": "simulation"`.

## Upgrade Ideas

- ESP32 or STM32 physical sensor node
- MQTT broker integration
- Time-series database
- Browser dashboard
- Email/notification alerts
- Rolling-average and trend-based fault detection
