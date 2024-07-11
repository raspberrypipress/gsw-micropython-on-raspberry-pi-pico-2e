import machine
import ssd1306

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

display.text("Hello, Pico!", 0, 0, 1)
display.show()