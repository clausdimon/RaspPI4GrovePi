from grovepi import *

def clearLight(green, red, blue):
    digitalWrite(green, 0)
    digitalWrite(red, 0)
    digitalWrite(blue, 0)