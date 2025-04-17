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

buttons_config = [
    {
        "label": "ETH - BB",
        "pin_mapping": { # out : in
            0:(0,),
            1:(1,),
            2:(2,),
            3:(3,),
            4:(4,),
            5:(5,),
            6:(6,),
            7:(7,)
        }
    },
    {
        "label": "ETH - SERVER",
        "pin_mapping": { # out : in
            0:(7,),
            1:(6,),
            2:(5,),
            3:(4,),
            4:(3,),
            5:(2,),
            6:(1,),
            7:(0,)
        }
    },
    {
        "label": "ETH - DATA",
        "pin_mapping": { # out : in
            0:(7,),
            1:(6,),
            2:(5,),
            3:(4,),
            4:(3,),
            5:(2,),
            6:(1,),
            7:(0,)
        }
    },
    {
        "label": "TEM - BB",
        "pin_mapping": { # out : in
            0:(7,),
            1:(6,),
            2:(5,),
            3:(4,),
            4:(3,),
            5:(2,),
            6:(1,),
            7:(0,)
        }
    }
]

    
def button_checker(x, y):
    global pages
    global page
    [btn.run(btn.x, btn.y) for _, btn in pages[page]["buttons"].items() if btn.is_in_region(x, y)]


def display_page(display, page):
    global pages
    display.clear()
    page_obj = pages[page]
    title = page_obj.get("title")
    if title:
        draw_header(display, title,color565(0,255,0), color565(0, 0, 0), color565(0, 255, 0))
    [btn.draw() for _, btn in page_obj["buttons"].items()]


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
        if set(res) == set(out_pins):
            icon = "V"
        display.draw_text(8, 28 * i, f"{i} > {str(res)[1:-1]}: {icon}", font, font_colour)
        pin_out_map[i].value(0)


def back_btn(display):
    global page
    page = HOME_PAGE
    display_page(display, page)

def draw_header(display, text,outline_color, bg_color, font_color):
    header_height = 40
    display.fill_hrect(0, 0, display.width, header_height, outline_color)
    display.fill_hrect(4, 4, display.width - 8, header_height - 8, bg_color)
    font = XglcdFont("Unispace12x24.c", 12, 24)
    text_width = len(text) * 12
    text_x = (display.width - text_width) // 2
    text_y = (header_height - 24) // 2
    display.draw_text(text_x, text_y, text, font, color=font_color, background=bg_color)

if __name__ == "__main__":
    display = mySetupX.createMyDisplay()
    display.clear()
    #display.draw_image("nyan_cat.raw", x=40, w=240)
    xptTouch = mySetupX.createXPT(button_checker)
    HOME_PAGE = "home"
    CONN_PAGE = "conn_page"
    
    pages = {
        HOME_PAGE: {
            "title": " | WINDSHEAR CABLE TESTER|",
            "buttons": {
                f"btn {row * 2 + col}": button(
                    display,
                    162 * col + 0,
                    77 * row + 44,
                    158,
                    73,
                    text=buttons_config[row*2+col]["label"],
                    task=cable_test,
                    task_args=(display, buttons_config[row*2+col]["pin_mapping"]),
                    font_colour=color565(0, 0, 0)
                )
                for row in range(2) for col in range(2)
            }
        },
        
        
        CONN_PAGE: {
            "title": " | ETHERNET -|",
            "buttons": {
                "Back": button(
                    display,
                    212,
                    182,
                    100,
                    50,
                    text="Back",
                    font_colour=color565(0, 0, 0),
                    task=back_btn,
                    task_args=(display,)
                )
            }
        }
    }
    
    #buttons["home"]["title"] = "WINDSHEAR CABLE TESTER"

    #buttons["home"]["btn 0"].task = cable_test
    #buttons["home"]["btn 0"].task_args = (display, straight_pin2pin_map)
    #buttons["home"]["btn 1"].task = cable_test
    #buttons["home"]["btn 1"].task_args = (display, cross_pin2pin_map)
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