from grovepi import *
from grove_rgb_lcd import *
import location as lO
import clearLight as cL
import tempeture as tE
import watering as wA
import enoughLight as eL
import sendToDatabase as sTD

rLed = 6
gLed = 5
bLed = 8
dht_sensor = 7
butn = 2
butn_changer = 3
light_sensor = 2
sound_Sensor = 1
potentiometer = 0

pinMode(rLed, "OUTPUT")
pinMode(gLed, "OUTPUT")
pinMode(bLed, "OUTPUT")
pinMode(butn, "INPUT")
pinMode(butn_changer, "INPUT")

i = 0
setRGB(240,248,250)
setText("")
sektion = lO.selcection(potentiometer, butn)
while True:
    try:
        setText("")
        cL.clearLight(gLed, rLed, bLed)
        light_intensity = analogRead(light_sensor)
        butn_presed = digitalRead(butn)
        if light_intensity <= 100:
            setText_norefresh(sektion + "\nNightTime")
        else:
            # if butn_presed:
                # sTD.send()
            # else:
                tE.tempeture(gLed, bLed, rLed, butn, sektion, butn_changer)
                i += 1
                if i%25 == 0:
                    wA.waterThemPlants(butn_changer)
                light_intensity = analogRead(light_sensor)
                if light_intensity <= 300 and light_intensity >100:
                    eL.moreLight(round(light_intensity/4), gLed, bLed, rLed)
                
    except (IOError, TypeError) as exceptErr:
        print("Error: ", exceptErr)
    except KeyboardInterrupt as ki:
        print(ki)
        setText_norefresh("")
