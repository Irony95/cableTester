from button import button
from ili9341 import Display, color565
from tools import draw_header
from tools import FONT


BUTTONS = [
    button(
        0,
        200,
        156,
        40,
        text="Back",
        task="result_page",
        task_args=(),
    )
]
icons = {True: "tick24x24.raw", False: "cross24x24.raw"}


def main(display: Display, test_profile: dict, results):
    TITLE = f"{test_profile['label']} (Details)"
    cable_pin_map = test_profile["cable_pin_map"]
    BUTTONS[0].task_args = (test_profile,)

    display.clear()
    draw_header(
        display, TITLE, color565(0, 255, 0), color565(0, 0, 0), color565(0, 255, 0)
    )
    [btn.draw(display) for btn in BUTTONS]

    for col in range(2):
        for row in range(4):
            i = col * 4 + row
            result = results[i]
            icon = icons[result]
            img_x, img_y = col * 150, 40 * row + 48
            text_x, text_y = img_x + 24, img_y
            display.draw_image(icon, img_x, img_y, 24, 24)
            if pin_pairing := cable_pin_map[i]:
                print(f" {','.join(pin_pairing[0])} > {','.join(pin_pairing[1])}")
                display.draw_text(
                    text_x,
                    text_y,
                    f" {','.join(pin_pairing[0])} > {','.join(pin_pairing[1])}",
                    FONT,
                    color565(0, 255, 0),
                )
            else:
                if result:
                    display.draw_text(text_x, text_y, "NIL", FONT, color565(0, 255, 0))
                else:
                    display.draw_text(
                        text_x, text_y, "SHORTED!", FONT, color565(0, 255, 0)
                    )
