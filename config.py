from machine import Pin

config = {
    "pin_in_map": { # read value
        0: Pin(16, Pin.IN),
        1: Pin(17, Pin.IN),
        2: Pin(18, Pin.IN),
        3: Pin(19, Pin.IN),
        4: Pin(20, Pin.IN),
        5: Pin(21, Pin.IN),
        6: Pin(22, Pin.IN),
        7: Pin(26, Pin.IN)
    },

    "pin_out_map": { # set value
        0: Pin(27, Pin.OUT),
        1: Pin(28, Pin.OUT),
        2: Pin(1, Pin.OUT),
        3: Pin(2, Pin.OUT),
        4: Pin(3, Pin.OUT),
        5: Pin(4, Pin.OUT),
        6: Pin(5, Pin.OUT),
        7: Pin(9, Pin.OUT)
    }    
}
