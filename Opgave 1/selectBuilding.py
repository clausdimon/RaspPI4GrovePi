from grovepi import *
from grove_rgb_lcd import *
import time


locations = ["Room 1", "Room 2", "Room 3", "Room 4", "Room 5", "Room 6", "Room 7", "Room 8", "Room 9", "Room 10"]
location = "MU8"



def selection(pM, butn):
    index = 0
    scale = 0
    while True:
        try:
            scale = analogRead(pM)
            butn_status = digitalRead(butn)

            if butn_status:
                global location
                location += " " + locations[index]
                setText_norefresh(location)
                return location
            else:
                if scale <= 100:
                    index = 0
                elif scale <= 200 and scale > 100:
                    index = 1
                elif scale <= 300 and scale > 200:
                    index = 2
                elif scale <= 400 and scale > 300:
                    index = 3
                elif scale <= 500 and scale > 400:
                    index = 4
                elif scale <= 600 and scale > 500:
                    index = 5
                elif scale <= 700 and scale > 600:
                    index = 6
                elif scale <= 800 and scale > 700:
                    index = 7
                elif scale <= 900 and scale > 800:
                    index = 8
                else:
                    index = 9
                
                setText_norefresh(locations[index])
        except IOError as ie:
            print(ie)
        except TypeError as te:
            print(te)


        

