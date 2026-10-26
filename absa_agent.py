import serial
import time

SERIAL_PORT = '/dev/ttyUSB0' 
BAUD_RATE = 9600

def run_absa_agent():
    print("=" * 65)
    print("  ABSA AGRI-AGENT: AUTONOMOUS SME CREDIT & ASSET VAULT ENGINE")
    print("  Security-by-Design | State-Machine Telemetry Stream Active")
    print("=" * 65)

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
        time.sleep(2) # Allow Arduino to reset and connect
        print("[AGENT STATUS]: Connected to hardware telemetry stream.\n")

        # Track vault state so we don't spam the servo motor
        last_vault_state = None

        while True:
            if ser.in_waiting > 0:
                raw_data = ser.readline().decode('utf-8', errors='ignore').strip()
                
                if "TELEMETRY:X_VAL:" in raw_data:
                    parts = raw_data.split(":")
                    x_val = int(parts[2])
                    btn_pressed = int(parts[4])

                    # Map joystick X-axis (0..1023) to an SME credit risk score (0..100%)
                    credit_request_level = int((x_val / 1023.0) * 100)

                    # Print live status cleanly
                    btn_label = "PRESSED" if btn_pressed == 1 else "IDLE"
                    print(f"\r[TELEMETRY] X: {x_val} | Credit: {credit_request_level}% | Button: {btn_label:<8}", end="")

                    # Autonomous AI Agent Decision Rule with State Machine
                    if credit_request_level > 70:
                        if last_vault_state != "UNLOCKED":
                            print("\n\n>>> [AGENT EVALUATION]: SME Credit Authorization Granted.")
                            print(">>> [AGENT ACTION]: Disbursing Micro-Credit Line & Unlocking Vault (90°)...")
                            ser.write(b"AGENT_ACTION:UNLOCK_VAULT\n")
                            last_vault_state = "UNLOCKED"
                            
                    elif credit_request_level < 30:
                        if last_vault_state != "LOCKED":
                            print("\n\n>>> [AGENT EVALUATION]: Credit Line Paused / Vault Secured.")
                            print(">>> [AGENT ACTION]: Securing Vault (0°)...")
                            ser.write(b"AGENT_ACTION:LOCK_VAULT\n")
                            last_vault_state = "LOCKED"

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n[AGENT STATUS]: Agent safely terminated.")
    except Exception as e:
        print(f"\n[ERROR]: Serial port connection error: {e}")

if __name__ == "__main__":
    run_absa_agent()