# 07 — Autonomous Firefighting Robot 🔥🤖

**Physical build — not a simulation.**

A mobile firefighting robot built from scratch as an embedded-systems project. The robot combines flame detection, obstacle sensing, autonomous movement, servo positioning and a water-pump extinguishing mechanism on a tracked chassis.

## What the Robot Does

1. Patrols/searches for a fire source.
2. Uses an ultrasonic sensor to detect obstacles.
3. Reads multiple flame sensors to determine the direction of a flame.
4. Drives the tracked chassis toward the target while avoiding collisions.
5. Positions the water outlet using servo control.
6. Activates the pump when the robot reaches an extinguishing position.
7. Returns to its search/navigation behaviour after the fire condition clears.

## Physical System

The completed prototype includes:

- Tracked mobile chassis
- Microcontroller-based controller
- Multi-direction flame sensing
- HC-SR04-style ultrasonic distance sensing
- DC motor drive system
- Servo-controlled mechanisms
- Water reservoir
- Electric water pump and tubing
- Battery-powered electronics

## System Architecture

```text
 Flame Sensors ---------\
                         \
 Ultrasonic Sensor -------> Microcontroller ---> Motor Driver ---> Tracks
                         /        |
 Other Inputs ----------/         +-----------> Servo Control
                                  |
                                  +-----------> Water Pump
```

## Control Strategy

```text
             +----------------+
             | SEARCH / PATROL |
             +-------+--------+
                     |
               flame detected
                     v
             +-------+--------+
             | LOCATE / ALIGN |
             +-------+--------+
                     |
               target reached
                     v
             +-------+--------+
             |   EXTINGUISH   |
             +-------+--------+
                     |
                flame cleared
                     v
             +-------+--------+
             | RESUME SEARCH  |
             +----------------+
```

Obstacle detection can interrupt navigation so the robot can change direction instead of driving directly into an object.

## Engineering Areas Demonstrated

- Embedded C/C++ programming
- Sensor interfacing
- Autonomous state-machine design
- Ultrasonic distance measurement
- Flame detection and directional decision logic
- DC motor control
- Servo positioning
- Pump/actuator control
- Power distribution
- Mechanical/electrical integration
- Hardware troubleshooting and iterative testing

## Why This Project Matters

Unlike the simulated test environments elsewhere in this portfolio, this is a **real physical prototype**. It demonstrates the complete engineering cycle: integrating sensors, firmware, actuators, mechanical hardware and power into a system that performs an observable task in the real world.

## Media

Photos and demonstration videos of the physical prototype are available and will be added to this folder as project media.

## Future Improvements

- Closed-loop flame localization
- Pump feedback / water-level sensing
- Battery voltage monitoring
- Wheel/track odometry
- Wireless telemetry
- Emergency stop and watchdog handling
- Improved enclosure and wiring harness
- Logged sensor data for debugging and validation
