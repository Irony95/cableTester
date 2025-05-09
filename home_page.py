from button import button
from config import TEST_PROFILES
from ili9341 import Display, color565
from tools import draw_header


TITLE = "WINDSHEAR CABLE TESTER"
BUTTONS = [
    button(
        164 * col + 0,
        76 * row + 48,
        156,
        68,
        text=TEST_PROFILES[row * 2 + col]["label"],
        task="result_page",
        task_args=(TEST_PROFILES[row * 2 + col],),
    )
    for row in range(2)
    for col in range(2)
]


def main(display: Display):
    # display.clear()
    draw_header(
        display, TITLE, color565(0, 255, 0), color565(0, 0, 0), color565(0, 255, 0)
    )
    [btn.draw(display) for btn in BUTTONS]
