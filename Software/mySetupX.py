from ili9341 import Display
from machine import Pin, SPI
from xpt2046 import Touch

TFT_CLK_PIN = const(6)
TFT_MOSI_PIN = const(7)

TFT_CS_PIN = const(13)
TFT_RST_PIN = const(14)
TFT_DC_PIN = const(15)

XPT_CLK_PIN = const(10)
XPT_MOSI_PIN = const(11)
XPT_MISO_PIN = const(8)

XPT_CS_PIN = const(12)
XPT_INT = const(0)

def createMyDisplay():
    spiTFT = SPI(0, baudrate=40000000, sck=Pin(TFT_CLK_PIN), mosi=Pin(TFT_MOSI_PIN))
    display = Display(spiTFT,
                      dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN),
                      width=320, height=240)
    return display

def createXPT(touch_handler):
    spiXPT = SPI(1, baudrate=1000000,
                 sck=Pin(XPT_CLK_PIN), mosi=Pin(XPT_MOSI_PIN), miso=Pin(XPT_MISO_PIN))

    # xpt = Touch(spiXPT, cs=Pin(XPT_CS_PIN), int_pin=Pin(XPT_INT),
    #             int_handler=touch_handler, x_min=219, x_max=1837, y_min=138, y_max=1895,
    #             width=320, height=240)
    xpt = Touch(spiXPT, cs=Pin(XPT_CS_PIN), int_pin=Pin(XPT_INT),
                int_handler=touch_handler, x_min=300, x_max=1807, y_min=210, y_max=1770,
                width=320, height=240)

    return xpt