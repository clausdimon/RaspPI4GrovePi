from grovepi import *

def highTemp(light):
    digitalWrite(light, 1)

def lowTemp(light):
    digitalWrite(light, 0)

def checkTemp(temp, light):
    if temp >= 23:
        highTemp(light)
    else:
        lowTemp(light)

