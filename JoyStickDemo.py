from microbit import *
import neopixel
np = neopixel.NeoPixel(pin0, 10)

atrest = Image("00000:"
               "00000:"
               "00900:"
               "00000:"
               "00000")
               
upfull = Image("00900:"
               "09590:"
               "99999:"
               "00900:"
               "00900")
               
uphalf = Image("00000:"
               "00900:"
               "09590:"
               "99999:"
               "00900:")
               
downfull = Image("00900:"
                 "00900:"
                 "99999:"
                 "09590:"
                 "00900")
                 
downhalf = Image("00900:"
                 "99999:"
                 "09590:"
                 "00900:"
                 "00000:")
                       
leftfull = Image("00900:"
                 "09900:"
                 "95999:"
                 "09900:"
                 "00900:")
                 
lefthalf = Image("00090:"
                 "00990:"
                 "09599:"
                 "00990:"
                 "00090:")

rightfull = Image("00900:"
                  "00990:"
                  "99959:"
                  "00990:"
                  "00900:")
  
righthalf = Image("09000:"
                  "09900:"
                  "99590:"
                  "09900:"
                  "09000:")
                  
AButton = Image("00990:"
                "09009:"
                "09000:"
                "09009:"
                "00990:")
                
BButton = Image("09990:"
                "09009:"
                "09009:"
                "09009:"
                "09990:")
               
while True:
    readingY = pin1.read_analog()
    readingX = pin2.read_analog()
        
    if ((readingY < 450) & (readingY > 250)):
        display.show(uphalf)
    elif (readingY < 251):
        display.show(upfull)
    elif ((readingY > 550) & (readingY < 750)):
        display.show(downhalf)
    elif (readingY > 749):
        display.show(downfull)
        
    elif ((readingX < 450) & (readingX > 250)):
        display.show(righthalf)
    elif (readingX < 251):
        display.show(rightfull)
        np[9] = (32,32,32)
        np[0] = (0,0,0)
        np.show()
    elif ((readingX > 550) & (readingX < 750)):
        display.show(lefthalf)
    elif (readingX > 749):
        display.show(leftfull)
        np[9] = (0,0,0)
        np[0] = (32,32,32)
        np.show()
        
    elif(pin16.read_digital() == 0):
        display.show(AButton)
        np[0] = (0,0,0)
        np[9] = (0,0,0)
        np.show()
    elif(pin12.read_digital() == 0):
        display.show(BButton)
        np[0] = (32,32,32)
        np[9] = (32,32,32)
        np.show()
    else:
        display.show(atrest)
        