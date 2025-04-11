from machine import Pin, SPI
from sys import implementation
from os import uname
import ili9341
from xglcd_font import XglcdFont
import mySetupX

print(implementation.name)
print(uname()[3])
print(uname()[4])

print(SPI(0))
print(SPI(1))

def xpt_touch(x, y):
    global xptTouch
    global minX, maxX, minY, maxY
    print(x, y)
    display.draw_text(0, 0, f"{x}, {y}    ", unispace,
                  ili9341.color565(255, 128, 0))

    display.fill_circle(x, y, 2, ili9341.color565(0, 255, 0))

display = mySetupX.createMyDisplay()
xptTouch = mySetupX.createXPT(xpt_touch)

print('Loading fonts...')
print('Loading unispace')
unispace = XglcdFont('Unispace12x24.c', 12, 24)

while True:
    pass

print("- bye -")
