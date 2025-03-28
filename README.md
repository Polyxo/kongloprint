## Automated print ejection using a Raspberry Pi and Balena

This tool is a work in progress

### Overview

This tool automates the print ejection process using a Raspberry Pi and Balena. It is compatible with the P1S printer and includes features for webcam monitoring and door control.

### Print files

The hinge for the motor can be found here:

https://makerworld.com/de/models/1250405-motorized-door-opener-for-p1s


### Features

- **Automated Print Ejection**: Automatically ejects prints upon completion.
- **Webcam Monitoring**: Allows real-time monitoring of the print process via a connected webcam.
- **Door Control**: Automates the opening and closing of the printer door.

### Requirements

- Raspberry Pi (any model with internet connectivity)
- Balena account
- P1S printer
- Webcam compatible with Raspberry Pi
- Necessary cables and connectors

### Installation

1. **Set up Raspberry Pi**: Install the latest version of Raspberry Pi OS.
2. **Create a Balena Application**: Sign up for a Balena account and create a new application.
3. **Deploy the Code**: Clone the repository and push the code to your Balena application.
4. **Connect the Hardware**: Connect the Raspberry Pi to the P1S printer and the webcam.

### Usage

1. **Start the Application**: Power on the Raspberry Pi and start the Balena application.
2. **Monitor the Print**: Use the webcam feed to monitor the print process.
3. **Automated Ejection**: Once the print is complete, the tool will automatically eject the print and open the printer door.

### Troubleshooting

- Ensure all connections are secure.
- Verify that the Raspberry Pi is connected to the internet.
- Check the Balena dashboard for any error messages.

### Contributing

Feel free to submit issues or pull requests to improve the tool.

### License

This project is licensed under the MIT License.
