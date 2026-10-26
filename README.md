# smart-SME-credit-vault
Smart SME Credit &amp; Asset Vault Engine—a prototype that bridges real-time financial decision-making with physical edge hardware actuation.

# Smart SME Credit & Asset Vault Engine

> **Absa GenAI-Thon 2026 Submission**  
> An edge-capable hardware/software prototype bridging real-time financial risk evaluation with physical actuator control.

---

## Project Overview
The **Smart SME Credit & Asset Vault Engine** evaluates synthetic SME credit telemetry and translates risk thresholds directly into physical security actuation (vault unlock/lock mechanisms). The core engine utilizes a non-blocking state-machine to prevent serial signal flooding and actuation jitter.

---

## System Architecture & Stack

### Hardware
* **Microcontroller:** Arduino Uno R3
* **Actuator:** SG90 Servo Motor
* **Telemetry Input:** Analog Joystick Module

### Software & Protocols
* **Host Platform:** Ubuntu Linux (ThinkPad)
* **Languages:** Python 3.12, C++ (Arduino Wiring)
* **Communication:** Serial Telemetry (`pySerial`) @ 9600 Baud
* **Logic Engine:** Non-blocking Finite State Machine (FSM)

---

## Key Technical Highlights
* **State Machine Actuation:** Implemented state-change detection to ensure servo sweep commands execute smoothly only on threshold transitions (0° vs 90°).
* **Robust Telemetry Parsing:** Handled noisy serial streams from microcontroller inputs with clean data sanitization.
* **Edge-First Design:** Designed to operate independently of continuous cloud availability for high-reliability environments.

---

## Developer
**Matibini Handiya**  
Third-Year Computer Systems Engineering Student  
University of Zambia (UNZA)  
* **Email:** handiyamatibeani@gmail.com[cite: 2]

* 
