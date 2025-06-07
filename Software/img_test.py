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
    img_width = 240
    i=0
    while True:
        img_x = i % img_width
        display.draw_image("nyan_cat.raw", x=img_x, w=img_width)
        i += 1