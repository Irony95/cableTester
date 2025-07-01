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
        text=TEST_PROFILES[row * 2 + col + 4]["label"],
        task="diagram_page",
        task_args=(TEST_PROFILES[row * 2 + col + 4],),
        colour=color565(255, 255, 0),
    )
    for row in range(2)
    for col in range(2)
    if row * 2 + col + 4 < len(TEST_PROFILES)
]
BUTTONS.extend(
    [
        button(
            0,
            200,
            98,
            40,
            text="<<<",
            task="home_page",
            colour=color565(255, 255, 255),
        ),
    ]
)


def main(display: Display):
    draw_header(
        display, TITLE, color565(0, 255, 0), color565(0, 0, 0), color565(0, 255, 0)
    )
    [btn.draw(display) for btn in BUTTONS]
