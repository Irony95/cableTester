from config import FONT
from ili9341 import Display


def draw_header(display: Display, text, outline_color, bg_color, font_color):
    header_height = 40
    display.fill_hrect(0, 0, display.width, header_height, outline_color)
    display.fill_hrect(4, 4, display.width - 8, header_height - 8, bg_color)
    text_width = len(text) * 12
    text_x = (display.width - text_width) // 2
    text_y = (header_height - 24) // 2
    display.draw_text(text_x, text_y, text, FONT, color=font_color, background=bg_color)
