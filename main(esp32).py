
#librerias
from machine import Pin, PWM
from time import sleep





#definicion de los servos 
servo1 = PWM(Pin(17), freq=50)#indice
servo2 = PWM(Pin(26), freq=50)#medio
servo3 = PWM(Pin(12), freq=50)#anular
servo4 = PWM(Pin(14), freq=50)#menique
servo5 = PWM(Pin(15), freq=50)#pulgar

#bucle de prueba
while True:
    lista = input("ingrese la lista")
    if lista[0] == "1":
        servo1.duty_ns(2400000)
    else:
        servo1.duty_ns(544000)
    if lista[1] == "1":
        servo2.duty_ns(2400000)
    else:
        servo2.duty_ns(544000)
    if lista[2] == "1":
        servo3.duty_ns(2400000)
    else:
        servo3.duty_ns(544000)
    if lista[3] == "1":
        servo4.duty_ns(2400000)
    else:
        servo4.duty_ns(544000)
    if lista[4] == "1":
        servo5.duty_ns(2400000)
    else:
        servo5.duty_ns(544000)
