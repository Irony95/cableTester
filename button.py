from ili9341 import color565
import mySetupX
from config import FONT


class button:
    def __init__(
        self,
        x,
        y,
        w,
        h,
        text=None,
        font_colour=None,
        colour=None,
        region=None,
        task=None,
        task_args=(),
    ) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.font_colour = font_colour
        self.region = region
        self.colour = colour
        self.font = FONT
        self.task = task
        self.task_args = task_args

        if self.text is not None:
            if self.h < 24:
                raise ValueError("Button not tall enough for text")
            if self.w < 12 * len(self.text):
                raise ValueError("Button not wide enough for text")
        if self.font_colour is None:
            self.font_colour = color565(0, 0, 0)
        if colour is None:
            self.colour = color565(0, 255, 0)
        if region is None:
            self.region = {"x_min": x, "x_max": x + w, "y_min": y, "y_max": y + h}

    def draw(self, display):
        display.fill_hrect(self.x, self.y, self.w, self.h, self.colour)
        if self.text is not None:
            text_x = round((self.w - 12 * len(self.text)) / 2 + self.x)
            text_y = round((self.h - 24) / 2 + self.y)
            display.draw_text(
                text_x,
                text_y,
                self.text,
                self.font,
                color=self.font_colour,
                background=self.colour,
            )

    def is_in_region(self, x, y):
        x_min = self.region["x_min"]
        x_max = self.region["x_max"]
        y_min = self.region["y_min"]
        y_max = self.region["y_max"]
        return (x_min <= x <= x_max) and (y_min <= y <= y_max)

    def run(self, x, y):
        print(f"hello! I am button ({self.x}, {self.y})")
        return self.task, self.task_args


def button_checker(x, y):
    global buttons
    [btn.run(btn.x, btn.y) for btn in buttons if btn.is_in_region(x, y)]


if __name__ == "__main__":
    display = mySetupX.createMyDisplay()
    display.clear()
    xptTouch = mySetupX.createXPT(button_checker)
    buttons = [
        button(
            8,
            58 * i + 8,
            200,
            50,
            text=f"btn {i}",
            font_colour=color565(0, 0, 0),
        )
        for i in range(4)
    ]

    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("shutting down...")
