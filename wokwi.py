from time import sleep
from machine import Pin

led=Pin(5,Pin.OUT)
led2=Pin(9,Pin.OUT)
led3=Pin(7,Pin.OUT)
while True:
    n= input()
    print(n)

    if n =='1':
        print('RED LED ON')
        led.value(1)
        sleep(1)
    if n == '2':
        print('BLUE LED ON')
        led2.value(2)
        sleep(2)
    if n =='3':
        print('GREEN LED ON')
        led3.value(3)
        sleep(3)
    if n == '0':
        print('LED OFF')
        led.value(0)
        led2.value(0)
        led3.value(0)
        
        