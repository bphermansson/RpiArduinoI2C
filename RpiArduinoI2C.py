# An Arduino is connected to the Rpi via I2C. As the Rpi has to be master we use an extra Gpio, this is 
# used by the Arduino to nofify the Rpi that is has something to say. 
# The Arduino pulls a pin high which creates an interrupt here (gpioInt) 
# The code then reads from the I2C bus. 
# http://wiki.minnowboard.org/Projects/AdaFruit_GPIO

import smbus
bus = smbus.SMBus(1)
import Adafruit_GPIO as GPIO
# The I2C address of the Arduino:
address = 0x04

def readNumber():
	number = bus.read_byte(address)
	print "Got " + str(number) + " from the Arduino."
	return number

def gpioInt(args):
	print "Interrupt!"
	# Read from I2C bus
	number = readNumber()

# Pin configuration.
pin = 17

# Create instance of GPIO for our platform 
myGPIO = GPIO.get_platform_gpio()

# Setup the pin for signal going in
myGPIO.setup(pin,GPIO.IN)

# Add interrupt 
myGPIO.add_event_detect(pin,GPIO.RISING,gpioInt,None)

# Do nothin but wait for interrupts
while True:
	pass

