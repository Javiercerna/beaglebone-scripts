import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

# IMPORTANT: Common anode LEDs!!! Supply with 3.3 V

# Constants
# ---------------------------------------------------------------------------

REDPIN = 'P9_14'
GREENPIN = 'P9_16'
BLUEPIN = 'P9_21'

# ---------------------------------------------------------------------------

# Methods
# ---------------------------------------------------------------------------

def setColor(red_value,green_value,blue_value):
    PWM.start(REDPIN,100-red_value*100.0/255) # Convert 0-100 to 0-255
    PWM.start(GREENPIN,100-green_value*100.0/255)
    PWM.start(BLUEPIN,100-blue_value*100.0/255)

# ---------------------------------------------------------------------------

# Main code

GPIO.setup(REDPIN,GPIO.OUT)
GPIO.setup(GREENPIN,GPIO.OUT)
GPIO.setup(BLUEPIN,GPIO.OUT)

while (True):
    try:
        print 'Turning on LED'
        setColor(255,0,0)
        time.sleep(1)
        setColor(0,255,0)
        time.sleep(1)
        setColor(0,0,255)
        time.sleep(1)
        setColor(255,255,255)
        time.sleep(1)
        setColor(170,0,255)
        time.sleep(1)
    except KeyboardInterrupt:
        break

print 'Turning off LED'
setColor(0,0,0)
