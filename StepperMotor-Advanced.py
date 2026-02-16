from machine import Pin
import time
IN1 = Pin(5,Pin.OUT)
IN2 = Pin(14,Pin.OUT)
IN3 = Pin(18,Pin.OUT)
IN4 = Pin(19,Pin.OUT)
pins = [IN1,IN2,IN3,IN4]
steps = [[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]]
while True:
    for a in steps:
        for i in range(4):
            pins[i].value(a[i])
        time.sleep_ms(5)

