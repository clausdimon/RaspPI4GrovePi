from grovepi import *
import time


def moreLight(lA, gLed, bLed, rLed):
    analogWrite(gLed, lA)
    analogWrite(bLed, lA)
    analogWrite(rLed, lA)
    time.sleep(5)
    digitalWrite(gLed,0)
    digitalWrite(bLed,0)
    digitalWrite(rLed,0)
    
