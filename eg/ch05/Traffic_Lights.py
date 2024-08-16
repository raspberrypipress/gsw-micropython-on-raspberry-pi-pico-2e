import machine
import time
import _thread

led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

button_pressed = False

def button_reader_thread():
    global button_pressed 
    while True:
        if button.value() == 1:
            button_pressed = True
        time.sleep(0.01)

_thread.start_new_thread(button_reader_thread, ())

while True:
    if button_pressed == True:
        led_red.value(1)
        for i in range(10):
            buzzer.value(1)
            time.sleep(0.04) 
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
