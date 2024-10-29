#!/usr/bin/env pybricks-micropython

# Before running this program, make sure the client and server EV3 bricks are
# paired using Bluetooth, but do NOT connect them. The program will take care
# of establishing the connection.

# The server (other program) must be started before the client (this program)!

from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.ev3devices import ColorSensor

ev3 = EV3Brick()
mail_color_sensor = ColorSensor(Port.S1)

# This is the name of the remote EV3 or PC we are connecting to.
SERVER = 'REPLACE WITH DEVICE NAME'

client = BluetoothMailboxClient()
mbox = TextMailbox('mail_color', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

# In this program, the client sends the first message and then waits for the
# server to reply.
while True:
    mbox.send(ColorSensor.color())