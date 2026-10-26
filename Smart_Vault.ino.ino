#include <Servo.h>

const int VRX_PIN = A0;   // Joystick X-axis connected to A0
const int SW_PIN = 2;     // Joystick Push Button connected to Digital Pin 2
const int SERVO_PIN = 3;  // Servo Motor Signal connected to Digital Pin 3

Servo vaultLock;

void setup() {
  Serial.begin(9600);
  pinMode(SW_PIN, INPUT_PULLUP); // Enable internal pullup for joystick button
  vaultLock.attach(SERVO_PIN);
  vaultLock.write(0); // Default position: LOCKED (0 degrees)
}

void loop() {
  int xVal = analogRead(VRX_PIN);
  int btnState = digitalRead(SW_PIN); // LOW when pressed

  // Send raw hardware telemetry over USB serial to ThinkPad
  Serial.print("TELEMETRY:X_VAL:");
  Serial.print(xVal);
  Serial.print(":BTN:");
  Serial.println(btnState == LOW ? 1 : 0);

  // Listen for decision commands sent back from the Python AI Agent
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "AGENT_ACTION:UNLOCK_VAULT") {
      vaultLock.write(90); // Rotate to UNLOCKED (90 degrees)
    } else if (command == "AGENT_ACTION:LOCK_VAULT") {
      vaultLock.write(0);  // Rotate to LOCKED (0 degrees)
    }
  }

  delay(200); // 5Hz telemetry sampling rate
}