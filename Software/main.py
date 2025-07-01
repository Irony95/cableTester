import mySetupX
from time import sleep_ms
import sys


if __name__ == "__main__":
    display = mySetupX.createMyDisplay()
    display.clear()
    display.draw_image("6AMB.raw", w=320)

    from pages import pages

    def button_checker(x, y):
        print(f"touch detected at {(x, y)}")
        global lock
        if not lock:
            global display
            global page
            global refresh
            global args
            global is_first_run
            for btn in pages[page].BUTTONS:
                if btn.is_in_region(x, y):
                    task, args = btn.run(x, y)
                    args = args
                    if task is not None:
                        page = task
                        page_obj = pages[page]
                        refresh = getattr(page_obj, "REFRESH", False)
                        is_first_run = True

    page = "home_page"
    args = ()
    refresh = False
    lock = False
    is_first_run = True

    sleep_duration = 0.02
    sleep_duration_ms = int(sleep_duration * 1000)
    polling_rate = int(1 / sleep_duration)
    refresh_rate = 2
    sleeps_per_sec = polling_rate * refresh_rate

    xptTouch = mySetupX.createXPT(button_checker)

    while True:
        try:
            if not lock and is_first_run:
                lock = True
                display.clear()
                pages[page].main(display, *args)
                is_first_run = False
                lock = False
            if refresh and not is_first_run:
                for _ in range(sleeps_per_sec):
                    if refresh and not is_first_run:
                        sleep_ms(sleep_duration_ms)
                    else:
                        break
                else:
                    if refresh and not is_first_run:
                        lock = True
                        pages[page].main(display, *args)
                        lock = False
        except KeyboardInterrupt:
            print("shutting down...")
            sys.exit(0)
