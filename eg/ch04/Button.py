import machine
import time

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button.value() == 0:
        print("You pressed the button!")
        time.sleep(2)
