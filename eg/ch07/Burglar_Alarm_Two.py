import machine
import time

snsr_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
snsr_pir2 = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)

def pir_handler(pin):
    time.sleep_ms(100)
    if pin.value():
        if pin is snsr_pir:
            print("ALARM! Motion detected in bedroom!")
        elif pin is snsr_pir2:
            print("ALARM! Motion detected in living room!")
        for i in range(50):
            led.toggle()
            buzzer.toggle()
            time.sleep_ms(100)

snsr_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
snsr_pir2.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.toggle()
    time.sleep(5)
