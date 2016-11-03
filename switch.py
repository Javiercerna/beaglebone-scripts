import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_13",GPIO.OUT)
while (True):
    try:
        GPIO.output("P9_13",GPIO.LOW)
        print 'P9_13 LOW'
        time.sleep(10)
        GPIO.output("P9_13", GPIO.HIGH)
        print 'P9_13 HIGH'
        time.sleep(10)
    except KeyboardInterrupt:
        break

print 'Cleaning up pins'
GPIO.cleanup()


