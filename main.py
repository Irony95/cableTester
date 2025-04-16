from machine import Pin
from os import uname
# import ili9341
from ili9341 import Display, color565
from xglcd_font import XglcdFont
import mySetupX
from time import sleep
from button_test import button


pin_in_map = { # read value
    0: Pin(16, Pin.IN),
    1: Pin(17, Pin.IN),
    2: Pin(18, Pin.IN),
    3: Pin(19, Pin.IN),
    4: Pin(20, Pin.IN),
    5: Pin(21, Pin.IN),
    6: Pin(22, Pin.IN),
    7: Pin(26, Pin.IN)
}

pin_out_map = { # set value
    0: Pin(27, Pin.OUT),
    1: Pin(28, Pin.OUT),
    2: Pin(1, Pin.OUT),
    3: Pin(2, Pin.OUT),
    4: Pin(3, Pin.OUT),
    5: Pin(4, Pin.OUT),
    6: Pin(5, Pin.OUT),
    7: Pin(9, Pin.OUT)
}


straight_pin2pin_map = { # out : in
    0:(0,),
    1:(1,),
    2:(2,),
    3:(3,),
    4:(4,),
    5:(5,),
    6:(6,),
    7:(7,)
}

cross_pin2pin_map = { # out : in
    0:(7,),
    1:(6,),
    2:(5,),
    3:(4,),
    4:(3,),
    5:(2,),
    6:(1,),
    7:(0,)
}

    
def button_checker(x, y):
    global buttons
    global page
    [btn.run(btn.x, btn.y) for _, btn in buttons[page].items() if btn.is_in_region(x, y)]


def display_page(display, page):
    global buttons
    display.clear()
    [btn.draw() for _, btn in buttons[page].items()]


def cable_test(display: Display, pin2pin_map: dict[int, tuple[int]]):
    global page
    page = CONN_PAGE
    display_page(display, page)
    font = XglcdFont("Unispace12x24.c", 12, 24)
    font_colour = color565(128, 128, 128)
    # while True:
    # display.clear()
    # display_page(display, page)
    
    # clear value
    [pin_out_map[i].value(0) for i in range(8)]


    for i in range(8):
        pin_out_map[i].value(1)
        res = []
        out_pins = pin2pin_map[i]
        for j in out_pins:
            if pin_in_map[j].value():
                res.append(j)
        icon = "X"
        if tuple(res) == out_pins:
            icon = "V"
        display.draw_text(8, 28 * i, f"{i} > {str(res)[1:-1]}: {icon}", font, font_colour)
        pin_out_map[i].value(0)


def back_btn(display):
    global page
    page = HOME_PAGE
    display_page(display, page)


if __name__ == "__main__":
    display = mySetupX.createMyDisplay()
    display.clear()
    display.draw_image("nyan_cat.raw", x=40, w=240)
    xptTouch = mySetupX.createXPT(button_checker)
    HOME_PAGE = "home"
    CONN_PAGE = "conn_page"
    buttons = {
        HOME_PAGE: {f"btn {i}":button(display, 8, 58 * i + 8, 100, 50, text=f"Btn {i}", font_colour=color565(0, 0, 0)) for i in range(4)},
        CONN_PAGE: {"Back": button(display, 212, 182, 100, 50, text="Back", font_colour=color565(0, 0, 0), task=back_btn, task_args=(display,))}
    }
    buttons["home"]["btn 0"].task = cable_test
    buttons["home"]["btn 0"].task_args = (display, straight_pin2pin_map)
    buttons["home"]["btn 1"].task = cable_test
    buttons["home"]["btn 1"].task_args = (display, cross_pin2pin_map)
    display.clear()
    display.draw_image("6AMB-2.raw", w=320)
    sleep(3)
    display.clear()
    page = HOME_PAGE
    display_page(display, page)
    
    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("shutting down...")
    # i=0
    # while True:
    #     img_x = i % img_width
    #     display.draw_image("nyan_cat.raw", x=img_x, w=img_width)
    #     i += 1