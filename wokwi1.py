from machine import Pin
import time

led = Pin(1, Pin.OUT)
button_pin = Pin(6, Pin.IN, Pin.PULL_UP)

while True:
    if (button_pin.value() == 0):
        
        if (led.value() == 0):   
            led.value(1)         
        else:                   
            led.value(0)        

        while (button_pin.value() == 0):
            time.sleep(0.05)
        
    time.sleep(0.05)