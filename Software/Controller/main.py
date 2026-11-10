import network
import time

SSID = "Luna"
PASSWORD = "Swan1811"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Connecting...")
wlan.connect(SSID, PASSWORD)

timeout = 10

while timeout > 0:
    if wlan.isconnected():
        break
    timeout -= 1
    print(".", end="")
    time.sleep(1)

if wlan.isconnected():
    print("\nConnected!")
    print("IP:", wlan.ifconfig()[0])
else:
    print("\nFailed to connect")


import socket
import time
from joystick import Joystick
from machine import *
from rotary_irq import RotaryIRQ
import json

# HOST = "192.168.4.52"
# PORT = 1313

class Client:
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))
        print("Connected!")

    def send(self, command):
        self.client.send(command.encode())

    def stop(self):
        self.client.close()

rotory1 = RotaryIRQ(
    pin_num_clk=2,
    pin_num_dt=1,
    min_val=-90,
    max_val=90,
    pull_up=True, reverse=True

)

joystick = Joystick(27, 26, 16)

client = Client("192.168.4.52", 1313)
time.sleep(1)

def convert(raw_value):
    left = raw_value[0] + raw_value[1]
    right = raw_value[0] - raw_value[1]
    return min(100, max(-100, left)), min(100, max(-100, right))

while True:
    left, right = convert(joystick.get_values())
    camera_angle = min(90, max(-90, rotory1.value()))
    command = (camera_angle, left, right)
    #print(f"Sending command: {command}")
    client.send(json.dumps(command))
    time.sleep(0.05)  # Adjust the sleep time as needed to control the sending rate