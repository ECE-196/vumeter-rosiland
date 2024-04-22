import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26,
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print(volume)

    volume_limits = [18000,21000,24000,27000,30000,33000,36000,39000,42000,45000,48000]

    for i in range(11):
        if volume > volume_limits[i]:
            leds[i].value = 1

    sleep(0.02)

    for i in range(10,0,-1):
        if volume < volume_limits[i]:
            leds[i].value = 0

