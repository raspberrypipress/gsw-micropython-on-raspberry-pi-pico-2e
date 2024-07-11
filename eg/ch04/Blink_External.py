import machine
import time

led_external = machine.Pin(15, machine.Pin.OUT)

while True:
    led_external.toggle()
    time.sleep(5)
