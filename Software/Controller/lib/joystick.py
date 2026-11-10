from machine import *
import time
from rotary_irq import RotaryIRQ

class Joystick:
    def __init__(self, x, y, btn):
        self.x = ADC(Pin(x, Pin.IN))
        self.y = ADC(Pin(y, Pin.IN))
        self.btn = Pin(btn, Pin.IN, Pin.PULL_DOWN)

    def get_values(self):
        return int(self.scale_axis(self.y.read_u16())), int(self.scale_axis(self.x.read_u16()))

    def scale_axis(self, raw_value):
        scaled = (raw_value - 32767) / 32767 * 100
        if abs(scaled) < 8:  # 8% deadzone works best for older joysticks
            return 0
        return scaled
