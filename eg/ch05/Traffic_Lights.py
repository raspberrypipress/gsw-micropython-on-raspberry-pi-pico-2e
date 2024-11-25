import machine
import time

led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
buzzer = machine.Pin(12, machine.Pin.OUT)

button_pressed = False

def btn_handler(pin):
    global button_pressed
    if not button_pressed:
        button_pressed = True

button.irq(trigger=machine.Pin.IRQ_FALLING, handler=btn_handler)

while True:
    if button_pressed == True:
        led_red.value(1)
        for i in range(20):
            buzzer.value(1)
            time.sleep(0.05)
            buzzer.value(0)
            time.sleep(0.2)
        button_pressed = False
    led_red.value(1)
    time.sleep(5)
    led_amber.value(1)
    time.sleep(2)
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    time.sleep(5)
    led_green.value(0)
    led_amber.value(1)
    time.sleep(5)
    led_amber.value(0)
