from grovepi import *
from grove_rgb_lcd import *
import tempeture as rTemp
import checkDb_lvl as rDb
import clearLight as cL
import selectBuilding as sB


redLed = 6
greenLed = 5
blueLed = 8
dht_sensor = 7
button = 2
button_changer = 3
light_sensor = 2
sound_sensor = 1
potentiometer = 0


pinMode(redLed, "OUTPUT")
pinMode(greenLed, "OUTPUT")
pinMode(blueLed, "OUTPUT")
pinMode(button, "INPUT")
pinMode(button_changer, "INPUT")

i = 0
setRGB(240,248,250)

building = sB.selection(potentiometer, button)
while True:
    try:
        cL.clearLight(greenLed, redLed, blueLed)
        light_intensity = analogRead(light_sensor)
        if light_intensity <= 250:
            setText_norefresh("NightTime")
            db = rDb.getdB(sound_sensor)
            if db >= 30:
                rDb.alarm(redLed, button)
        else:
            i = analogRead(potentiometer)
            butn_status = digitalRead(button)
            if butn_status:
                if i <= 300:
                    rDb.checkNoise(sound_sensor, greenLed, blueLed, redLed, button)
                elif i <= 600 and i > 300:
                    rTemp.tempeture(sound_sensor, greenLed, blueLed, redLed, button, building, button_changer)
                else:
                    setText_norefresh("Choose Something")
            else:
                if i <= 300:
                    setText_norefresh("check Noise")
                elif i <= 600 and i > 300:
                    setText_norefresh("check Tempeture")
                else:
                    setText_norefresh("nothing chosen")

    except (IOError, TypeError) as e:
        print("Error: " + e)
    except KeyboardInterrupt as ki:
        print(ki)
        cL.clearLight(greenLed, redLed, blueLed)
        setText_norefresh("")