import machine
import ssd1306

mosi = machine.Pin(11)
sck = machine.Pin(10)
res = machine.Pin(14)
dc = machine.Pin(12)
cs = machine.Pin(13)

spi = machine.SPI(1, 100000, mosi=mosi, sck=sck)
display = ssd1306.SSD1306_SPI(128, 64, spi, dc, res, cs)

display.text("Hello World!", 0, 0, 1)
display.show()