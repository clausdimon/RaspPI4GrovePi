from typing import IO
from grovepi import *
from grove_rgb_lcd import *
import time
import json

dht_sensor = 7
tempC 
tempF

def lightOn(light):
    digitalWrite(light, 1)
def lightOff(light):
    digitalWrite(light, 0)
def checkTemp(temp, gLed, bLed, rLed):
    if temp >= 25:
        lightOn(rLed)
        lightOff(gLed)
        lightOff(bLed)
        time.sleep(1)
    elif temp <= 15:
        lightOn(bLed)
        lightOff(gLed)
        lightOff(rLed)
        time.sleep(1)
    else:
        lightOn(gLed)
        lightOff(bLed)
        lightOff(rLed)
        time.sleep(1)

def tempeture(glight, blight, rlight, butn, place, butn_change):
    celcius = True
    try:
        butn_pressed = digitalRead(butn)
        butn_changed = digitalRead(butn_change)
        if butn_changed:
            if celcius == True:
                celcius = False
            elif celcius == False:
                celcius = True

        [temp, hum] = dht(dht_sensor, 0)
        checkTemp(temp, glight, blight, rlight)
        if celcius == False:
            global tempC
            global tempF
            tempC = temp
            tempF = temp*1.8 + 32
            t = str(round(tempF))
            h = str(hum)
            setText_norefresh(t + "F " + h + "%\n" + place)
            tempToJson(tempC, tempF, place)
        else:
            global tempC
            global tempF
            tempC = temp
            tempF = temp*1.8 + 32
            t = str(tempC)
            h = str(hum)
            setText_norefresh(t + "C " + h + "%\n" + place)
            tempToJson(tempC, tempF, place)
            
    except IOError as ie:
        print(ie)
    except TypeError as te:
        print(te)
def tempToJson(tC, tF, sektion):
    data = {}
    data['temperature'] =  []
    data["temperature"].append({
        'tempC': tC,
        'tempF': tF,
        'location': sektion
    })

    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    
    