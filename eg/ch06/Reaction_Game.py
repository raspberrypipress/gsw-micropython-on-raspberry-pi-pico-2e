import machine
import time
import random

button_pressed = False
led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

def btn_handler(pin):
    global button_pressed
    if not button_pressed:
        button_pressed = True
        print(pin)

led.value(1)
time.sleep(random.uniform(5, 10))
led.value(0)
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=btn_handler)
