import machine
import time

led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button.value() == 0:
        led_external.value(1)
        time.sleep(2)
    led_external.value(0)
