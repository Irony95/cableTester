from machine import Pin, SPI
from random import random, seed
from ili9341 import Display, color565
from utime import sleep_us, ticks_cpu, ticks_us, ticks_diff
import mySetupX

display = mySetupX.createMyDisplay()

display.clear()

display.fill_hrect(10,10, 10, 10, color565(255, 0, 0))

display.fill_hrect(300, 230, 10, 10, color565(0, 255, 0))

