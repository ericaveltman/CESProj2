# CESProj2

## What You Need 
### Software
- Sonic Pi<br />
`https://sonic-pi.net/`
- Python 3
- Arduino IDE<br />

### Hardware
For this project, I used a Raspberry Pi 3B+, ESP32, 2 buttons, a switch and a joystick. The buttons each will play a different sample, the switch will activate reverb and the joysticks Y-axis will change the pitch of whatever sound you play.
### Connections:
Button #1: Using two pins from the same side of the button,I connected one to Ground on the breadboard and the other to GPIO 25.<br/>
Button #2: Using two pins from the same side of the button,I connected one to Ground on the breadboard and the other to GPIO 33.<br/>
Switch: I connected the center pin to Ground on the breadboard and one of the other pins to GPIO 18.<br/>
Joystick: I connected GND to Ground, +5V to power on the breadboard, VRX to GPIO 13, VRY to GPIO 12 and SW to GPIO 14.<br/>
## How To Run (Step by Step):
### ESP32 code<br />
Upload the .io file to your ESP32 (or other micro controller). Make sure that you find the correct port that is being used. The way I did this on the Raspberry Pi was by using the command <br/>
`ls /dev/tty*`<br/>
Run the command and then unplug your ESP32. Whichever one dissapears is the port the your ESP32 was using.
### Python
Replace the port on line 8 with whatever port your ESP32 is using. Then run the python script
### Sonic Pi
Load the .rb file into Sonic Pi. Then press 'Run' and you should have sound!

