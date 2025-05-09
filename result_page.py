from button import button
from config import PIN_IN_MAP, PIN_OUT_MAP
from ili9341 import Display, color565
from tools import draw_header


REFRESH = True
TEST_PROFILE = None
ARGS = (TEST_PROFILE,)
BUTTONS = [
    button(0, 200, 156, 40, text="Back", task="home_page"),
    button(
        164,
        200,
        156,
        40,
        text="Details",
        task="details_page",
        task_args=(),
    ),
]


def main(display: Display, test_profile: dict):
    TEST_PROFILE = test_profile
    TITLE = TEST_PROFILE["label"]
    out_to_in_pin_map = TEST_PROFILE["out_to_in_pin_map"]

    # display.clear()
    draw_header(
        display, TITLE, color565(0, 255, 0), color565(0, 0, 0), color565(0, 255, 0)
    )
    [btn.draw(display) for btn in BUTTONS]

    # clear value
    [PIN_OUT_MAP[i].value(0) for i in range(8)]

    results = []
    for i in range(8):
        PIN_OUT_MAP[i].value(1)
        detected = []
        for j in range(8):
            if PIN_IN_MAP[j].value():
                detected.append(j)
        is_pass = set(detected) == set(out_to_in_pin_map[i])
        results.append(is_pass)
        print(f"{i} > {str(detected)[1:-1]}: {is_pass}")
        PIN_OUT_MAP[i].value(0)

    img_x, img_y = (display.width - 64) // 2, (display.height - 64) // 2
    if sum(results) == 8:
        display.draw_image("tick64x64.raw", img_x, img_y, 64, 64)
    else:
        display.draw_image("cross64x64.raw", img_x, img_y, 64, 64)

    details_btn = BUTTONS[1]
    details_btn.task_args = (TEST_PROFILE, results)
