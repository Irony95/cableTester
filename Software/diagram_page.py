from button import button
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
]


def main(display: Display, test_profile: dict):
    TITLE = test_profile["label"]

    draw_header(
        display, TITLE, color565(0, 255, 0), color565(0, 0, 0), color565(0, 255, 0)
    )
    [btn.draw(display) for btn in BUTTONS]


    test_btn = BUTTONS[1]
    test_btn.task_args = (test_profile,)
