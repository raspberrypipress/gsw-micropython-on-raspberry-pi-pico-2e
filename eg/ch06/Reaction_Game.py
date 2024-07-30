import machine
import time
import random

pressed = False
led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

def btn_handler(pin):
    global pressed
    if not pressed:
        pressed = True
        print(pin)

led.value(1)
time.sleep(random.uniform(5, 10))
led.value(0)
button.irq(trigger=machine.Pin.IRQ_RISING, handler=btn_handler)

time.sleep(1)  # Gives some time before the program ends
