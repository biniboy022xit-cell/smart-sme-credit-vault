# Smart SME Credit & Asset Vault Engine

> **Absa GenAI-Thon 2026 submission.** A hardware-software prototype that links a simulated credit score to a physical lock mechanism.

---

## Overview

This prototype demonstrates how a financial decision can trigger a physical action. An Arduino streams input values over serial to a Python program on a laptop. The program converts the input into a 0-100 "credit request" score, applies decision rules, and sends lock or unlock commands back to the Arduino, which turns a servo "vault lock."

**What is simulated:** the credit score comes from an analog joystick, standing in for real SME credit data. The decision logic is a simple threshold rule, not a machine-learning model. The project shows the end-to-end loop (sensor, decision, actuator), not a production credit engine.

[Demo video](https://github.com/user-attachments/assets/e5e94463-a937-4266-b062-0039907355aa)

---

## How it works

1. **Arduino Uno** reads the joystick X-axis and button every 200 ms and sends a line over serial: `TELEMETRY:X_VAL:<value>:BTN:<0|1>`.
2. **Python host** (`Absa_agent.py`, using pySerial) reads each line and maps the X value (0-1023) to a score from 0 to 100.
3. **Decision rule with a dead-band:**
   - Score above 70: send `AGENT_ACTION:UNLOCK_VAULT`
   - Score below 30: send `AGENT_ACTION:LOCK_VAULT`
   - Score between 30 and 70: keep the current state (prevents flickering near a single threshold)
4. **State-change detection:** the host remembers the last vault state and sends a command only when it changes, so the servo is not commanded on every reading.
5. **Arduino** receives the command and moves the SG90 servo to 90 degrees (unlocked) or 0 degrees (locked).

---

## Hardware and software

| Part | Details |
|------|---------|
| Microcontroller | Arduino Uno R3 |
| Actuator | SG90 servo (vault lock) |
| Input | Analog joystick module (simulated credit input) |
| Host | Ubuntu Linux laptop, Python 3.12 |
| Communication | Serial at 9600 baud (pySerial) |
| Firmware | C++ (Arduino framework) |

The decision logic runs on the host laptop, not on the Arduino, and needs no internet connection.

---

## Known limitations

I list these so it is clear what the prototype does and does not do.

- **No AI or ML model.** The "agent" is a threshold rule with hysteresis. A real system would use actual credit data and a trained model.
- **Simulated input.** A joystick stands in for SME credit telemetry.
- **Fragile serial parsing.** A corrupted line can raise an error that stops the host program. Parsing should be wrapped in its own error handling so bad lines are skipped.
- **Blocking firmware delay.** The Arduino uses `delay(200)` to set its sample rate, so it only checks for commands every 200 ms. A `millis()`-based timer would be non-blocking.
- **Button value unused.** The button state is transmitted but does not affect decisions.
- **Hard-coded serial port.** The port name is set in the code and may need changing on another machine.

---

## Possible next steps

- Replace the joystick with real or realistic synthetic credit data
- Add a simple model for the score instead of a fixed mapping
- Make serial parsing robust and the firmware non-blocking
- Add a physical or logged confirmation step before unlocking

---

## Developer

**Matibini Handiya**
Third-year Computer Science student (Computer Systems Engineering focus), University of Zambia (UNZA)
Email: handiyamatibeani@gmail.com
