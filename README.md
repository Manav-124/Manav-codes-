# Engineering Systems Lab

A hands-on portfolio of embedded systems, hardware validation, automated testing, robotics, diagnostics, and IoT engineering.

This repository is organized like a small engineering lab rather than a collection of unrelated demos. It combines a **real autonomous firefighting robot prototype** with reproducible hardware-test and embedded-system projects.

> **Portfolio integrity:** Physical projects are identified as physical builds. Software-only measurement sources are explicitly labeled as simulated.

## ⭐ Featured Physical Build

### Autonomous Firefighting Robot
A tracked embedded robot built from scratch to detect flames, navigate around obstacles, align with a target and operate a water-pump extinguishing mechanism.

**Embedded C/C++ · flame sensing · ultrasonic sensing · motor control · servos · pump control · autonomous state machine · hardware integration**

➡️ [`projects/07-autonomous-firefighting-robot`](projects/07-autonomous-firefighting-robot)

## Lab Projects

| # | Project | Focus | Main Technologies |
|---|---|---|---|
| 01 | Automated Hardware Validation Bench | Automated electrical tests and pass/fail reports | Python, instrument-adapter design, CSV |
| 02 | STM32 Sensor Health Monitor | Embedded sensing and fault-state firmware | C, STM32, ADC, UART, state machines |
| 03 | Production Test Station | Manufacturing test and unit traceability | Python, SQLite, test sequencing |
| 04 | IoT Equipment Monitor | Telemetry and equipment-health monitoring | Python, MQTT concepts, JSON |
| 05 | Signal & Fault Analyzer | Signal statistics and anomaly screening | Python, signal metrics |
| 06 | Embedded Safety Controller | Multi-sensor safety logic | C/C++, Arduino/STM32 concepts |
| **07** | **Autonomous Firefighting Robot** | **Real robotic prototype built from scratch** | **C/C++, sensors, motors, servos, pump** |

## Engineering Skills Demonstrated

- Embedded C/C++ and microcontroller state machines
- Physical sensor, actuator and mechanical integration
- Hardware troubleshooting methodology
- Oscilloscope, DMM and power-supply test concepts
- Automated validation and repeatable test procedures
- Python test automation and data analysis
- UART, ADC, GPIO and sensor interfacing
- Production test sequencing and traceability
- Failure classification and structured diagnostics
- Technical documentation and Git workflow

## Repository Structure

```text
projects/
├── 01-hardware-validation-bench/
├── 02-stm32-sensor-monitor/
├── 03-production-test-station/
├── 04-iot-equipment-monitor/
├── 05-signal-fault-analyzer/
├── 06-embedded-safety-controller/
└── 07-autonomous-firefighting-robot/   <-- physical build

docs/
└── ENGINEERING_NOTES.md
```

## Design Philosophy

**Sense / Acquire → Decide / Validate → Act / Diagnose → Record → Improve**

The portfolio is aimed at hardware test, validation, electronics, embedded systems, production test, systems integration and junior hardware engineering work.

## Getting Started

```bash
git clone https://github.com/Manav-124/Manav-codes-.git
cd Manav-codes-
python3 projects/01-hardware-validation-bench/validation_bench.py
```

## Roadmap

- Add firefighting robot build photos and demo video
- Add full robot firmware and pin map
- Add real serial-instrument adapter for bench equipment
- Add automated unit tests and CI
- Add captured hardware measurements
- Add test-history dashboard

## About

An engineering portfolio focused on practical embedded systems, robotics, hardware testing, automation and diagnostics.
