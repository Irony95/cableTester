from config import FONT
from ili9341 import Display


def draw_header(display: Display, text, outline_color, bg_color, font_color):
    header_height = 40
    display.fill_hrect(0, 0, display.width, header_height, outline_color)
    display.fill_hrect(4, 4, display.width - 8, header_height - 8, bg_color)
    text_width = len(text) * 12
    text_x = round((display.width - text_width) / 2)
    text_y = round((header_height - 24) / 2)
    display.draw_text(text_x, text_y, text, FONT, color=font_color, background=bg_color)


def fill_super_ellipse(display: Display, x, y, w, h, colour):
    def ellipse(a):
        return lambda x, y: (x / a) ** 5 + (y / a) ** 5

    if w % 2:
        a = int((w - 1) / 2)
        x_centering = 0
    else:
        a = int(w / 2)
        x_centering = -1
    if h % 2:
        b = int((h - 1) / 2)
        y_centering = 0
    else:
        b = int(h / 2)
        y_centering = -1

    x0, y0 = x + a, y + b
    min_r = b
    x_stretch = 0
    y_stretch = 0

    if a > b:
        x_stretch += a - b
    elif a < b:
        min_r = a
        y_stretch += b - a

    x, y = 0, min_r
    my_elps = ellipse(min_r)

    display.draw_vline(x0, y0 - b, 2 * b + y_centering + 1, colour)
    display.draw_hline(x0 - a, y0, 2 * a + x_centering + 1, colour)

    for i in range(1, x_stretch + 1):
        display.draw_vline(
            x0 - i, y0 - min_r, 2 * min_r + y_centering + 1, colour
        )
        display.draw_vline(
            x0 + i, y0 - min_r, 2 * min_r + y_centering + 1, colour
        )

    # for i in range(2 * min_r + x_centering + 1):
    for i in range(1, y_stretch + 1):
        display.draw_hline(
            x0 - min_r, y0 - i, 2 * min_r + x_centering + 1, colour
        )
        display.draw_hline(
            x0 - min_r, y0 + i, 2 * min_r + x_centering + 1, colour
        )

    while min_r > x:
        x += 1
        if my_elps(x, y - 0.5) > 1:
            y -= 1

        display.draw_vline(
            x0 - x - x_stretch,
            y0 - y - y_stretch,
            2 * (y + y_stretch) + y_centering + 1,
            colour,
        )
        display.draw_vline(
            x0 + x + x_stretch + x_centering,
            y0 - y - y_stretch,
            2 * (y + y_stretch) + y_centering + 1,
            colour,
        )
        display.draw_hline(
            x0 - y - x_stretch,
            y0 - x - y_stretch,
            2 * (y + x_stretch) + x_centering + 1,
            colour,
        )
        display.draw_hline(
            x0 - y - x_stretch,
            y0 + x + y_stretch + y_centering,
            2 * (y + x_stretch) + x_centering + 1,
            colour,
        )
        if x >= y:
            break
