from machine import Pin, SPI
from sys import implementation
from os import uname
from random import randint
# import ili9341
from ili9341 import Display, color565
from xglcd_font import XglcdFont
import mySetupX
import time



if __name__ == "__main__":
    display = mySetupX.createMyDisplay()
    display.clear()
    i=0
    while True:
        display.draw_image("nyan_cat.raw", x=i % 320, w=240)
        # time.sleep(0.2)
        i += 1