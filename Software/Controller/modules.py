from machine import *
import time
from rotary_irq import RotaryIRQ

class Joystick:
    def __init__(self, x, y, btn):
        self.x = ADC(Pin(x, Pin.IN))
        self.y = ADC(Pin(y, Pin.IN))
        self.btn = Pin(btn, Pin.IN, Pin.PULL_DOWN)

    def prin(self):
        print(f"X: {int(self.x.read_u16()/100)}")
        print(f"Y: {int(self.y.read_u16()/100)}")
        print(f"BTN: {self.btn.value()}")

rotory1 = RotaryIRQ(
    pin_num_clk=2,
    pin_num_dt=1,
    min_val=0,
    max_val=100,
    pull_up=True, reverse=True

)

while True:
    print(rotory1.value())