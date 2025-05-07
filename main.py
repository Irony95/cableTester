import mySetupX
from time import sleep
import sys


if __name__ == "__main__":
    display = mySetupX.createMyDisplay()
    display.clear()
    display.draw_image("6AMB.raw", w=320)

    from pages import pages

    def button_checker(x, y):
        global display
        global page
        global refresh
        global args
        for btn in pages[page].BUTTONS:
            if btn.is_in_region(x, y):
                task, args = btn.run(x, y)
                args = args
                if task is not None:
                    page = task
                    page_obj = pages[page]
                    refresh = getattr(page_obj, "REFRESH", False)
                    return pages[page].main(display, *args)

    xptTouch = mySetupX.createXPT(button_checker)
    page = "home_page"
    refresh = False
    args = ()
    pages[page].main(display, *args)

    while True:
        try:
            if refresh:
                sleep(3)
                pages[page].main(display, *args)
        except KeyboardInterrupt:
            print("shutting down...")
            sys.exit(0)
