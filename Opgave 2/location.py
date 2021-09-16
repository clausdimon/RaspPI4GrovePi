from threading import stack_size
from grovepi import *
from grove_rgb_lcd import *
import time

locations = ["Sektion 1", "Sektion 2", "Sektion 3", "Sektion 4", "Sektion 5"]
location = "Drivhus"
current_Choosen = ""
next_Choosing = ""

def selcection(pM, butn):
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
                if scale <=200:
                    index = 0
                elif scale <= 400 and scale > 200:
                    index = 1
                elif scale <= 600 and scale > 400:
                    index = 2
                elif scale <= 800 and scale > 600:
                    index = 3
                else:
                    index  = 4
                
                global current_Choosen
                global next_Choosing
                current_Choosen = locations[index]
                next_Choosing = "  " + locations[index+1] if len(locations) > index+1 else ""
                setText_norefresh("->" + current_Choosen + "\n" + next_Choosing)
                time.sleep(2)
        except IOError as ie:
            print(ie)
        except TypeError as te:
            print(te)