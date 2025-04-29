from ili9341 import Display, color565
from xglcd_font import XglcdFont
import mySetupX
from time import sleep
from button_test import button
from config import config


buttons_config = [
    {
        "label": "ETH - BB",
        "pin_mapping": {  # out : in
            0: (0,),
            1: (1,),
            2: (2,),
            3: (3,),
            4: (4,),
            5: (5,),
            6: (6,),
            7: (7,),
        },
    },
    {
        "label": "ETH - SERVER",
        "pin_mapping": {  # out : in
            0: (7,),
            1: (6,),
            2: (5,),
            3: (4,),
            4: (3,),
            5: (2,),
            6: (1,),
            7: (0,),
        },
    },
    {
        "label": "ETH - DATA",
        "pin_mapping": {  # out : in
            0: (7,),
            1: (6,),
            2: (5,),
            3: (4,),
            4: (3,),
            5: (2,),
            6: (1,),
            7: (0,),
        },
    },
    {
        "label": "TEM - BB",
        "pin_mapping": {  # out : in
            0: (7,),
            1: (6,),
            2: (5,),
            3: (4,),
            4: (3,),
            5: (2,),
            6: (1,),
            7: (0,),
        },
    },
]


def button_checker(x, y):
    global pages
    global page
    [
        btn.run(btn.x, btn.y)
        for _, btn in pages[page]["buttons"].items()
        if btn.is_in_region(x, y)
    ]


def display_page():
    global display
    global pages
    global page
    display.clear()
    title = pages[page].get("title")
    if title:
        draw_header(
            display, title, color565(0, 255, 0), color565(0, 0, 0), color565(0, 255, 0)
        )
    [btn.draw() for _, btn in pages[page]["buttons"].items()]


def cable_test(display: Display, draw_page, pin2pin_map: dict[int, tuple[int]]):
    global page
    page = draw_page
    display_page()
    font = XglcdFont("Unispace12x24.c", 12, 24)
    font_colour = color565(128, 128, 128)

    # clear value
    [PIN_OUT_MAP[i].value(0) for i in range(8)]

    res = True
    for i in range(8):
        PIN_OUT_MAP[i].value(1)
        detected = []
        out_pins = pin2pin_map[i]
        for j in out_pins:
            if PIN_IN_MAP[j].value():
                detected.append(j)
        if set(detected) == set(out_pins):
            icon = "V"
            res &= True
        else:
            icon = "X"
            res &= False
        print(f"{i} > {str(detected)[1:-1]}: {icon}")
        PIN_OUT_MAP[i].value(0)
    

def back_btn(draw_page):
    global page
    page = draw_page
    display_page()


def draw_header(display, text, outline_color, bg_color, font_color):
    header_height = 40
    display.fill_hrect(0, 0, display.width, header_height, outline_color)
    display.fill_hrect(4, 4, display.width - 8, header_height - 8, bg_color)
    font = XglcdFont("Unispace12x24.c", 12, 24)
    text_width = len(text) * 12
    text_x = (display.width - 8 - text_width) // 2
    text_y = (header_height - 24) // 2
    display.draw_text(text_x, text_y, text, font, color=font_color, background=bg_color)


if __name__ == "__main__":
    display = mySetupX.createMyDisplay()
    display.clear()
    xptTouch = mySetupX.createXPT(button_checker)
    PIN_IN_MAP = config["pin_in_map"]
    PIN_OUT_MAP = config["pin_out_map"]

    pages: dict = {
        "home": {
            "title": "WINDSHEAR CABLE TESTER",
            "buttons": {
                f"btn {row * 2 + col}": button(
                    display,
                    162 * col + 0,
                    77 * row + 44,
                    158,
                    73,
                    text=buttons_config[row * 2 + col]["label"],
                    task=cable_test,
                    task_args=("conn", buttons_config[row * 2 + col]["pin_mapping"]),
                    font_colour=color565(0, 0, 0),
                )
                for row in range(2)
                for col in range(2)
            },
        },
        "conn": {
            "title": "ETHERNET",
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
                    task_args=("home"),
                )
            },
        },
    }

    display.clear()
    display.draw_image("6AMB-2.raw", w=320)
    sleep(3)
    display.clear()
    page = "home"
    display_page()

    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("shutting down...")
