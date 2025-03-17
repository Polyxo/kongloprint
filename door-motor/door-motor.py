import time
import pigpio
from flask import Flask

# Initialize Flask for a simple API
app = Flask(__name__)

# Connect to the pigpio daemon
pi = pigpio.pi()

# Servo GPIO pin (Adjust if necessary)
SERVO_PIN = 18

# Open/Close Positions (Adjust based on your servo)
OPEN_POSITION = 1900  # Adjust if necessary
CLOSE_POSITION = 2500  # Adjust if necessary

def move_servo(position):
    """Move the servo to the given position."""
    if pi.connected:
        pi.set_servo_pulsewidth(SERVO_PIN, position)
        time.sleep(1)  # Allow time for the servo to move
        pi.set_servo_pulsewidth(SERVO_PIN, 0)  # Stop signal
        return f"Servo moved to {position}"
    else:
        return "pigpio daemon not running!"

@app.route('/open', methods=['GET'])
def open_door():
    return move_servo(OPEN_POSITION)

@app.route('/close', methods=['GET'])
def close_door():
    return move_servo(CLOSE_POSITION)

if __name__ == "__main__":
    print("Starting door motor API...")
    app.run(host='0.0.0.0', port=3000)  # Run Flask on all network interfaces
