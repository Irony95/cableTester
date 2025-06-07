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

minX = maxX = minY = maxY = 500

def xpt_touch(x, y):
    global xptTouch
    global minX, maxX, minY, maxY

    if x != 0:
        if x > maxX:
            maxX = x
        elif x < minX:
            minX = x
    if y != 0:    
        if y > maxY:
            maxY = y
        elif y < minY:
            minY = y
    
    display.fill_circle(x, y, 2, ili9341.color565(0, 255, 0))
    print(str(x) + ":" + str(y))
    
    # display.fill_circle(touchX, touchY, 2, ili9341.color565(255, 0, 0))
    # print(str(touchX) + ":" + str(touchY))
        
    xReading = "X: " + str(minX) + " - " + str(maxX) + "       "
    yReading = "Y: " + str(minY) + " - " + str(maxY) + "       "
        
    display.draw_text(0, 100, xReading, unispace,
                  ili9341.color565(255, 128, 0))
    display.draw_text(0, 125, yReading, unispace,
                  ili9341.color565(255, 128, 0))

display = mySetupX.createMyDisplay()
xptTouch = mySetupX.createXPT(xpt_touch)

print('Loading fonts...')
print('Loading unispace')
unispace = XglcdFont('Unispace12x24.c', 12, 24)

display.draw_text(0, 0, ili9341.__name__, unispace,
                  ili9341.color565(255, 128, 0))
display.draw_text(0, 25, ili9341.implementation.name, unispace,
                  ili9341.color565(0, 0, 200))
display.draw_text(0, 50, str(ili9341.implementation.version), unispace,
                  ili9341.color565(0, 0, 200))

while True:
    pass

print("- bye -")