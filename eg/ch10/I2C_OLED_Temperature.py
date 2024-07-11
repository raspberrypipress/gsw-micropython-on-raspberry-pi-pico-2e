import machine
import ssd1306
import time

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

adc = machine.ADC(4)
conversion_factor = 3.3 / (65535)
while True:
    reading = adc.read_u16() * conversion_factor
    temperature = 25 - (reading - 0.706)/0.001721
    display.fill(0)
    display.text(f"Temp: {temperature}", 0, 0, 1)
    display.show()
    time.sleep(2)
