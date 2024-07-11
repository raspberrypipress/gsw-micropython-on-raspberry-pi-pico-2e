import machine
import time

potentiometer = machine.ADC(26)
conversion_factor = 3.3 / (65535)

while True:
    voltage = potentiometer.read_u16() * conversion_factor
    print(voltage)
    time.sleep(2)
