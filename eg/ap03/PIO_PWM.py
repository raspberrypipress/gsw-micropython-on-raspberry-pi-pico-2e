from rp2 import PIO, StateMachine, asm_pio
from machine import Pin
import utime

@asm_pio(set_init=PIO.OUT_LOW)
def quarter_bright():
    set(pins, 0) [2]
    set(pins, 1)

@asm_pio(set_init=PIO.OUT_LOW)
def half_bright():
    set(pins, 0)
    set(pins, 1)

@asm_pio(set_init=PIO.OUT_HIGH)
def full_bright():
    set(pins, 1)

led = Pin("LED")
sm1 = StateMachine(1, quarter_bright, freq=10000, set_base=led)
sm2 = StateMachine(2, half_bright, freq=10000, set_base=led)
sm3 = StateMachine(3, full_bright, freq=10000, set_base=led)

while(True): 
    sm1.active(1)
    utime.sleep(1)
    sm1.active(0)

    sm2.active(1)
    utime.sleep(1)
    sm2.active(0)

    sm3.active(1)
    utime.sleep(1)
    sm3.active(0)
