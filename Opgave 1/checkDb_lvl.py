from grovepi import *
from grove_rgb_lcd import *
import time

def getdB(sound_sensor):
    sound_lvl = analogRead(sound_sensor)
    db_lvl = round((sound_lvl+83.2073) / 11.003)
    return db_lvl

def highNoise(redLight):
    digitalWrite(redLight, 1)
    digitalWrite(redLight,0)
    digitalWrite(redLight, 1)
    digitalWrite(redLight,0)
    

def lowNoise(blueLight):
    digitalWrite(blueLight, 1)
    digitalWrite(blueLight, 0)
    digitalWrite(blueLight, 1)
    digitalWrite(blueLight, 0)
    

def perfectNoise(greenLight):
    digitalWrite(greenLight, 1)
    digitalWrite(greenLight, 0)
    digitalWrite(greenLight, 1)
    digitalWrite(greenLight, 0)

def checkNoise(sound, greenLight, blueLight, redLight, butn):
    highSounds = 0
    while True:
        db_lvl = getdB(sound)
        butn_status = digitalRead(butn)
        if butn_status:
            break
        else:
            if db_lvl >= 46:
                highNoise(redLight)
                highSounds +=1
                setText_norefresh("To much Noise: " +  str(highSounds))
            elif db_lvl <= 20:
                lowNoise(blueLight)
                setText_norefresh("Quited level of Noise")
            else:
                perfectNoise(greenLight)
                setText_norefresh("Perfect level of Noise")
def alarm(redLight, butn):
    while True:
        butn_pressed = digitalRead(butn)

        if butn_pressed:
            break
        else:
            digitalWrite(redLight, 1)
            digitalWrite(redLight, 0)
