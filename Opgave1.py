from grovepi import *
from grove_rgb_lcd import *
import tempeture as rTemp


redLed = 6
greenLed = 5
blueLed = 8
dht_sensor = 7
button = 2
light_sensor = 2
sound_sensor = 1
potentiometer = 0


pinMode(redLed, "OUTPUT")
pinMode(greenLed, "OUTPUT")
pinMode(blueLed, "OUTPUT")
pinMode(button, "INPUT")

i = 0
setRGB(240,248,250)
while True:
    try:
        [temp, hum] = dht(dht_sensor, 0)
        light_intensity = analogRead(light_sensor)
        sound_lvl = analogRead(sound_sensor)
        db_lvl = round((sound_lvl+83.2073) / 11.003)
        print (db_lvl,  " ", sound_lvl)
        print("temp: ", temp, "C\thumidity: ", hum, "%")
        t = str(temp)
        h = str(hum)
        rTemp.checkTemp(temp, redLed)
        setText_norefresh(t + " C " + h + "%\n" + str(db_lvl))

    except (IOError, TypeError) as e:
        print("Error")