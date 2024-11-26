import machine
import time

snsr_pir = machine.Pin(28, machine.Pin.IN)
led = machine.Pin(15, machine.Pin.OUT)

def pir_handler(pin):
    time.sleep_ms(100)
    if pin.value():
        print("ALARM! Motion detected!")
        for i in range(50):
            led.toggle()
            time.sleep_ms(100)

snsr_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
