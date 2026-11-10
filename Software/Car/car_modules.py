from gpiozero import PWMOutputDevice as PWM
from gpiozero import OutputDevice as Pin
from math import floor
from gpiozero import AngularServo

class Motor:
        def __init__(self, forward, backward, ena):
                self.ena_pin = PWM(ena)
                self.forward_pin = Pin(forward)
                self.backward_pin = Pin(backward)
                self.forward_pin.off()
                self.backward_pin.off()
                self.ena_pin.value = 0.5

        def forward(self):
                self.backward_pin.off()
                self.forward_pin.on()

        def backward(self):
                self.forward_pin.off()
                self.backward_pin.on()

        def stop(self):
                self.backward_pin.off()
                self.forward_pin.off()

class DriveTrain:
        def __init__(self, motor1, motor2):
                self.motor1 = motor1
                self.motor2 = motor2

        def set_speed(self, left, right):
                self.motor1.ena_pin.value = left/100
                self.motor2.ena_pin.value = right/100

        def drive(self, left, right):
                if left <= 0 and right <= 0:
                        self.motor1.backward()
                        self.motor2.backward()
                        self.set_speed(abs(left), abs(right))
                elif left >= 0 and right >= 0:
                        self.motor1.forward()
                        self.motor2.forward()
                        self.set_speed(left, right)
                elif left <= 0 and right >= 0:
                        self.motor1.backward()
                        self.motor2.forward()
                        self.set_speed(abs(left), right)
                elif left >= 0 and right <= 0:
                        self.motor1.forward()
                        self.motor2.backward()
                        self.set_speed(left, abs(right))
                







