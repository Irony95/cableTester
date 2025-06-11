from machine import Pin


PIN_IN_MAP = {  # read value
    0: Pin(16, Pin.IN),
    1: Pin(17, Pin.IN),
    2: Pin(18, Pin.IN),
    3: Pin(19, Pin.IN),
    4: Pin(20, Pin.IN),
    5: Pin(21, Pin.IN),
    6: Pin(22, Pin.IN),
    7: Pin(26, Pin.IN),
}
PIN_OUT_MAP = {  # set value
    0: Pin(27, Pin.OUT),
    1: Pin(28, Pin.OUT),
    2: Pin(1, Pin.OUT),
    3: Pin(2, Pin.OUT),
    4: Pin(3, Pin.OUT),
    5: Pin(4, Pin.OUT),
    6: Pin(5, Pin.OUT),
    7: Pin(9, Pin.OUT),
}
out_to_in_pin_map = {  # out : in
    0: (0,),
    1: (1,),
    2: (2,),
    3: (3,),
    4: (4,),
    5: (5,),
    6: (6,),
    7: (7,),
}


# clear value
[PIN_OUT_MAP[i].value(0) for i in range(8)]

results = []
for i in range(8):
    print("#" * 64)
    out_pin = PIN_OUT_MAP[i]
    print(i, out_pin)
    out_pin.value(1)
    detected = []
    for j in range(8):
        in_pin = PIN_IN_MAP[j]
        print(f"\t{j, in_pin}, {in_pin.value()}")
        if in_pin.value():
            detected.append(j)
    is_pass = set(detected) == set(out_to_in_pin_map[i])
    print(f"\t{detected=}, expected={out_to_in_pin_map[i]}, {is_pass=}")
    results.append(is_pass)
    out_pin.value(0)
print("#" * 64)
