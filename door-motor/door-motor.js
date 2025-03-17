const Gpio = require("pigpio").Gpio;
const express = require("express");

const app = express();
const port = 80;

// Servo motor setup
const servo = new Gpio(18, { mode: Gpio.OUTPUT });
const openPosition = 2500;
const closePosition = 500;

function moveServo(position) {
  servo.servoWrite(position);
  setTimeout(() => servo.servoWrite(0), 1000);
}

app.get("/open", (req, res) => {
  console.log("Opening door...");
  moveServo(openPosition);
  res.send("Door Opened!");
});

app.get("/close", (req, res) => {
  console.log("Closing door...");
  moveServo(closePosition);
  res.send("Door Closed!");
});

app.listen(port, () => {
  console.log(`Door motor service running on port ${port}`);
});
