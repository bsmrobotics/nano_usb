# NANO USB
A simple library for controlling the Funduino board from your computer
## Getting Started
`import nano_usb as nu`
Then attach the board to the correct port on your computer.
`nu.setup('name_of_port')`
For example
`nu.setup('/dev/ttyusb0')`

## Controlling Servo Motors
`nu.servoWrite(pin_number, angle)`
`angle` should be between 0 and 180, but will depend slightly on your specific servo motor.
For example
`nu.servoWrite(3, 150)`

## Reading Digital Sensors
`nu.digitalRead(pin_number)`
For example
`nu.digitalRead(8)`
This will return True of False
