from gpiozero import Device
from gpiozero.pins.pigpio import PiGPIOFactory

Device.pin_factory = PiGPIOFactory()

import time
from modules import *
import json

#socket setup
import socket

HOST = '0.0.0.0'
PORT = 1313

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Waiting for connection...")

client, addr = server.accept()
print("Connected:", addr)

motor1 = Motor(19, 13, 6) #left
motor2 = Motor(17, 27, 22) #right
camera_servo = AngularServo(
    12,
    min_angle=-90,
    max_angle=90
)
car = DriveTrain(motor1, motor2)

while True:
        try:
                data = client.recv(1024)

                if not data:
                    print('no data')
                    break
                try:
                        command = tuple(json.loads(data))
                except:
                       pass
                try:
                    if int(command[0]) < 90 or int(command[0]) > -90:
                        camera_servo.angle = int(command[0])
                except:
                    pass
                print(command)
                car.drive(int(command[1]), int(command[2]))

        except Exception as e:
                print(e)
                break
client.close()
server.close()

                                                                                      