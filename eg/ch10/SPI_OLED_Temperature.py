import machine
import ssd1306
import time

mosi = machine.Pin(11)
sck = machine.Pin(10)
res = machine.Pin(14)
dc = machine.Pin(12)
cs = machine.Pin(13)

spi = machine.SPI(1, 100000, mosi=mosi, sck=sck)
display = ssd1306.SSD1306_SPI(128, 64, spi, dc, res, cs)

adc = machine.ADC(4)
conversion_factor = 3.3 / (65535)
while True:
    reading = adc.read_u16() * conversion_factor
    temperature = 25 - (reading - 0.706)/0.001721
    display.fill(0)
    display.text(f"Temp: {temperature}", 0, 0, 1)
    display.show()
    time.sleep(2)
