from machine import Pin, SPI
from sys import implementation
from os import uname
from random import randint
# import ili9341
from ili9341 import Display, color565
from xglcd_font import XglcdFont
import mySetupX


class button:
    def __init__(self, x, y, w, h, colour=None, region=None) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.region = region
        self.colour = colour
        if colour is None:
            self.colour = color565(0, 255, 0)
        if region is None:
            self.region = {
                "x_min": x,
                "x_max": x + w,
                "y_min": y,
                "y_max": y + h
            }
        self.draw()

    def draw(self):
        display.fill_hrect(self.x, self.y, self.w, self.h, self.colour)
    
    def is_in_region(self, x, y):
        x_min = self.region["x_min"]
        x_max = self.region["x_max"]
        y_min = self.region["y_min"]
        y_max = self.region["y_max"]
        return (x_min <= x <= x_max) and (y_min <= y <= y_max)

    def run(self, x, y):
       self.colour = color565(randint(0, 255), randint(0, 255), randint(0, 255))
       self.draw()
       print(f"hello! I am button ({x},{y})")


def button_checker(x, y):
    global buttons
    [btn.run(btn.x, btn.y) for btn in buttons if btn.is_in_region(x, y)]


display = mySetupX.createMyDisplay()
display.clear()
xptTouch = mySetupX.createXPT(button_checker)
buttons = [button(8, (8+50) * i +8, 100, 50) for i in range(4)]

while True:
    try:
        pass
    except KeyboardInterrupt:
        print("shutting down...")