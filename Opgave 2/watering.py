from grove_rgb_lcd import *
from grovepi import *

def waterThemPlants(butn):
    while True:
        try:
            setText_norefresh("You need to water \nthem Plants Boy!")
            butn_status = digitalRead(butn)
            if butn_status:
                break
        except (IOError, TypeError) as exceptErr:
            print("Error: ", exceptErr)
        except KeyboardInterrupt as kI:
            print(kI)
            setText_norefresh("")

