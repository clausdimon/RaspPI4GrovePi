from grovepi import *
from grove_rgb_lcd import *
import checkDb_lvl as sound
import time

dht_sensor = 7

def highTemp(light):
    digitalWrite(light, 1)

def notHighTemp(light):
    digitalWrite(light, 0)

def lowTemp(light):
    digitalWrite(light, 0)

def notLowTemp(light):
    digitalWrite(light, 0)

def rightTemp(light):
    digitalWrite(light, 1)

def notRightTemp(light):
    digitalWrite(light, 0)

def checkTemp(temp, greenLight, blueLight, redLight):
    if temp >= 23:
        highTemp(redLight)
        notLowTemp(blueLight)
        notRightTemp(greenLight)
    elif temp <= 15:
        notHighTemp(redLight)
        notRightTemp(greenLight)
        lowTemp(blueLight)
    else:
        rightTemp(greenLight)
        notLowTemp(blueLight)
        notHighTemp(redLight)


def tempeture(sound_sensor, green, blue, red, butn, building, butn_change):
    celcius = True
    while True:
        try:
            butn_pressed = digitalRead(butn)
            butn_changed = digitalRead(butn_change)

            if butn_pressed:
                break
            else:
                if butn_changed:
                    if celcius == True:
                        celcius = False
                    elif celcius == False:
                        celcius = True
                db_lvl = sound.getdB(sound_sensor)
                [temp, hum] = dht(dht_sensor, 0)
                checkTemp(temp, green, blue, red)
                if celcius == False:
                    temp  = temp*1.8 + 32
                    print("temp: ", round(temp), "F\thumidity: ", hum, "%")
                    t = str(round(temp))
                    h = str(hum)
                    setText_norefresh(t + "F " + h + "% " + str(db_lvl)+ "dB\n" + building)
                else:
                    print("temp: ", temp, "C\thumidity: ", hum, "%")
                    t = str(temp)
                    h = str(hum)
                    setText_norefresh(t + "C " + h + "% " + str(db_lvl)+ "dB\n" + building)
                
        except IOError as e:
            print(e)
        except TypeError as tE:
            print(tE)
        