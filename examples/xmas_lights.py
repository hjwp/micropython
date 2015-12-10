from microbit import *

xmaspixels = [
    (0, 4),
    (1, 1), (1, 3), (1, 4),
    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
    (3, 1), (3, 3), (3, 4),
    (4, 4)
    ]

def tree():
    for x, y in xmaspixels:
        display.set_pixel(x, y, 3)


def flashing():
    while not button_b.is_pressed():
        #tuple unpacking
        x, y = xmaspixels[random(len(xmaspixels))]
        display.set_pixel(x, y, random(7) + 3)
        x, y = xmaspixels[random(len(xmaspixels))]
        display.set_pixel(x, y, 3)
        sleep(200)

tree()
while True:
    if button_a.is_pressed():
        flashing()
        tree()
