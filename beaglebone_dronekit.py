import Adafruit_BBIO.UART as UART
import serial
from dronekit import connect, VehicleMode

# Constants
# ----------------------------------------------------------------------------

UART_NAME = 'UART1'
PORT = '/dev/ttyO1'
BAUDRATE = 57600

# ----------------------------------------------------------------------------

# Main code

UART.setup(UART_NAME)

print 'Connecting to vehicle on %s' % PORT
vehicle = connect(ip=PORT,wait_ready=True,baud=BAUDRATE)

# Get some vehicle attributes (state)
print 'Get some vehicle attribute values:'
print 'GPS: %s' % vehicle.gps_0
print 'Battery: %s' % vehicle.battery
print 'Last Heartbeat: %s' % vehicle.last_heartbeat
print 'Is Armable?: %s' % vehicle.is_armable
print 'System status: %s' % vehicle.system_status.state
print 'Mode: %s' % vehicle.mode.name    # settable

while (True):
    try:
        print 'Mode: %s' % vehicle.mode.name
    except KeyboardInterrupt:
        break

# Close vehicle object before exiting script
vehicle.close()
print 'Vehicle disconnected'

#ser = serial.Serial(port=PORT,baudrate=BAUDRATE)
#ser.close()
#ser.open()

#if ser.isOpen():
#    print 'Serial is open!'
#    ser.write('Hello')

#ser.close()
