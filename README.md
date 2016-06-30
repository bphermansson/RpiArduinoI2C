# RpiArduinoI2C

This project demonstrates I2C communication between a Raspberry Pi and an Arduino. The Rpi can only be used as a I2C master and the Arduino has to be used as a slave. This means the Rpi must initiate all communication, the Arduino normally cant tell the Rpi it has something to say. In this project a neat trick is used to get by this. The two devices are not just connected via I2C, we also connect a Gpio from one unit to the other. When the Arduino has something to say it rises this pin to a high level. The code on the Rpi detects this and asks the Arduino what she has to say, thus initiating the communication. In practice this means the Arduino acts as kind of fake host with ability to initiate communications.

Connections
The SDA and SCL lines on both devices are connected directly. This is possible even if the Arduino is a 5 volt device (according to https://oscarliang.com/raspberry-pi-arduino-connected-i2c/). The Gpio:s has to be connected via a level converter. As the communication is one way it can be a simple resistor divider, I use 2k2 and 3k3 resistors. The 2k2 connects to the Arduino Gpio and to the 3k3 resistor which then is connected to ground. The Rpi Gpio is connected to the resistor midpoint which gives a high at about 3 volt, suitable for the Rpi. 

Usage

