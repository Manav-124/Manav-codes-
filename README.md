# Engineering Systems Lab — 20 Project Portfolio

A practical portfolio covering **embedded systems, hardware validation, robotics, automated testing, diagnostics, communications and IoT engineering**.

The centerpiece is a **real autonomous firefighting robot built from scratch**. Software-only measurement projects use clearly identified demo/simulated data so the portfolio stays technically honest and interview-ready.

## ⭐ Featured Physical Build — Autonomous Firefighting Robot

Tracked embedded robot designed to sense flames, detect obstacles, control drive motors, position an extinguishing mechanism and operate a water pump.

**C/C++ · flame sensing · ultrasonic sensing · motor drivers · servos · pump control · autonomous state machine · hardware integration**

➡️ [`projects/07-autonomous-firefighting-robot`](projects/07-autonomous-firefighting-robot)

## 20 Engineering Projects

| # | Project | Engineering Focus |
|---|---|---|
| 01 | [Automated Hardware Validation Bench](projects/01-hardware-validation-bench) | Automated measurements, limits and reports |
| 02 | [STM32 Sensor Health Monitor](projects/02-stm32-sensor-monitor) | ADC, UART and embedded state machines |
| 03 | [Production Test Station](projects/03-production-test-station) | Manufacturing test and traceability |
| 04 | [IoT Equipment Monitor](projects/04-iot-equipment-monitor) | Telemetry and equipment health |
| 05 | [Signal & Fault Analyzer](projects/05-signal-fault-analyzer) | Signal statistics and fault screening |
| 06 | [Embedded Safety Controller](projects/06-embedded-safety-controller) | Multi-sensor safety logic |
| **07** | **[Autonomous Firefighting Robot](projects/07-autonomous-firefighting-robot)** | **Physical robotics build** |
| 08 | [UART Device Diagnostic Tool](projects/08-uart-device-diagnostic-tool) | Serial telemetry diagnostics |
| 09 | [Power Rail Supervisor](projects/09-power-rail-supervisor) | Multi-rail tolerance validation |
| 10 | [Sensor Calibration Engine](projects/10-sensor-calibration-engine) | Measurement calibration |
| 11 | [Test Log Failure Analyzer](projects/11-test-log-failure-analyzer) | Failure-mode ranking |
| 12 | [Digital Logic Testbench](projects/12-digital-logic-testbench) | Truth-table verification |
| 13 | [PWM Motor Controller](projects/13-pwm-motor-controller) | Embedded motor control |
| 14 | [Thermal Stress Monitor](projects/14-thermal-stress-monitor) | Thermal validation |
| 15 | [CAN Bus Health Monitor](projects/15-can-bus-health-monitor) | Vehicle/industrial bus diagnostics |
| 16 | [I2C Device Scanner](projects/16-i2c-device-scanner) | Embedded peripheral discovery |
| 17 | [Firmware Watchdog Simulator](projects/17-firmware-watchdog-simulator) | Firmware reliability |
| 18 | [Battery Health Estimator](projects/18-battery-health-estimator) | Power-system diagnostics |
| 19 | [Networked Test Jig Protocol](projects/19-networked-test-jig) | Connected production fixtures |
| 20 | [Hardware Regression Runner](projects/20-hardware-regression-runner) | Baseline vs current validation |

## Core Skills Demonstrated

**Embedded:** C, C++, STM32 concepts, Arduino concepts, ADC, UART, GPIO, PWM, I2C, CAN, state machines  
**Test & Validation:** DMM/oscilloscope concepts, limit testing, regression, calibration, traceability, failure analysis  
**Automation:** Python, SQLite, CSV/JSON, automated reports, test sequencing  
**Systems:** sensors, motors, servos, power rails, telemetry, test-jig architecture, fault diagnosis

## Engineering Workflow

```text
SENSE / ACQUIRE
      ↓
VALIDATE / DECIDE
      ↓
ACT / DIAGNOSE
      ↓
RECORD / REPORT
      ↓
IMPROVE / REGRESSION TEST
```

## Portfolio Integrity

The firefighting robot is presented as a physical build. Projects using generated measurements are demonstration/simulation implementations and are not represented as laboratory measurements. Each is structured so a physical hardware adapter can be added later.

## Getting Started

```bash
git clone https://github.com/Manav-124/Manav-codes-.git
cd Manav-codes-
python3 projects/01-hardware-validation-bench/validation_bench.py
```

## Next Up

- Add firefighting robot build media and complete firmware
- Add physical STM32/Arduino captures
- Add automated unit tests and GitHub Actions
- Add instrument interfaces and richer reports
- Add hardware architecture diagrams

## About

Engineering portfolio focused on the practical intersection of **hardware + firmware + testing + automation**.
