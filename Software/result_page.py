from time import sleep_ms

from button import button
from config import PIN_IN_MAP, PIN_OUT_MAP
from ili9341 import Display, color565
from tools import draw_header

# REFRESH = True
# TEST_PROFILE = None
# ARGS = (TEST_PROFILE,)
BUTTONS = [
    button(
        0,
        200,
        98,
        40,
        text="Back",
        task="home_page",
        colour=color565(255, 255, 255),
    ),
    button(
        111,
        200,
        98,
        40,
        text="Test",
        task="result_page",
        task_args=(),
        colour=color565(255, 255, 0),
    ),
    button(
        222,
        200,
        98,
        40,
        text="Details",
        task="details_page",
        task_args=(),
        colour=color565(255, 255, 255),
    ),
]


def main(display: Display, test_profile: dict):
    TITLE = test_profile["label"]

    draw_header(
        display, TITLE, color565(0, 255, 0), color565(0, 0, 0), color565(0, 255, 0)
    )
    [btn.draw(display) for btn in BUTTONS]

    # clear value
    [PIN_OUT_MAP[i].value(0) for i in range(8)]

    out_to_in_pin_map = test_profile["out_to_in_pin_map"]
    pin_delay_ms = 10
    results = []
    for i in range(8):
        print("#" * 64)
        out_pin = PIN_OUT_MAP[i]
        print(i, out_pin)
        out_pin.value(1)
        sleep_ms(pin_delay_ms)

        detected = []
        for j in range(8):
            in_pin = PIN_IN_MAP[j]
            print(f"\t{j, in_pin}, {in_pin.value()}")
            if in_pin.value():
                detected.append(j)
        is_pass = set(detected) == set(out_to_in_pin_map[i])
        print(f"\t{detected=}, expected={out_to_in_pin_map[i]}, {is_pass=}")
        results.append(is_pass)
        
        out_pin.value(0)
        sleep_ms(pin_delay_ms)
    print("#" * 64)

    img_x, img_y = (display.width - 64) // 2, (display.height - 64) // 2
    if sum(results) == 8:
        display.draw_image("tick64x64.raw", img_x, img_y, 64, 64)
    else:
        display.draw_image("cross64x64.raw", img_x, img_y, 64, 64)

    test_btn = BUTTONS[1]
    test_btn.task_args = (test_profile,)
    details_btn = BUTTONS[2]
    details_btn.task_args = (test_profile, results)
