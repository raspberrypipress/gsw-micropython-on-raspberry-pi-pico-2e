import machine
import time
import random

button_pressed = False
led = machine.Pin(15, machine.Pin.OUT)
left_btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
right_btn = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
fastest_btn = None

def btn_handler(pin):
    global button_pressed
    if not button_pressed:
        button_pressed = True
        global fastest_btn
        fastest_btn = pin

led.value(1)
time.sleep(random.uniform(5, 10))
led.value(0)
start_time = time.ticks_ms()
left_btn.irq(trigger=machine.Pin.IRQ_FALLING, handler=btn_handler)
right_btn.irq(trigger=machine.Pin.IRQ_FALLING, handler=btn_handler)
while fastest_btn is None:
    time.sleep(1)
if fastest_btn is left_btn:
    print("Left Player wins!")
elif fastest_btn is right_btn:
    print("Right Player wins!")
