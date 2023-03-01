from pyautogui import *
import time
import random

Random = ['z','q','s','d','4','left','right','down', 'up', '1','2','3','4']
MME_Mode = 'false'

print("Apex Farming Tool for MME is started")


while True:

     if locateOnScreen('./img/LaunchHomeScreen.png', region=(800,600,1150,750), grayscale=True, confidence=0.7) != None:
          click(x=952, y=717)
          print("HomeScreen OK")
          time.sleep(5)

     if locateOnScreen('./img/MME_NewsOnStart.png', region=(0,0,1920,100), grayscale=True, confidence=0.7) != None:
               press('esc')
               print("News OK")
               time.sleep(3)


     if (locateOnScreen('./img/MME_SelectModeTrios.png', region=(0,700,450,910), grayscale=True, confidence=0.7) and MME_Mode == 'false') != None:
               time.sleep(1)
               moveTo(240, 820)
               time.sleep(1)
               doubleClick()
               print("Detected Trio")


     if (locateOnScreen('./img/MME_MenuMode.png', region=(0,0,1920,1080), grayscale=True, confidence=0.7) and MME_Mode == 'false') != None:
               time.sleep(1)
               moveTo(1020, 580)
               doubleClick()
               time.sleep(1)
               MME_Mode = 'true'
               print("Select MME OK")



     if (locateOnScreen('./img/ready.png', region=(0,538,447,528), grayscale=True, confidence=0.7) and MME_Mode == 'true' ) != None:
          moveTo(230, 950)
          click()
          print("Preparing for ready")
          time.sleep(1)
          
     
                
     if locateOnScreen('./img/cancel_ready.png', region=(0,538,447,528), grayscale=True, confidence=0.7) != None:
         print("Waiting for game")
         time.sleep(5)
    
     if locateOnScreen('./img/MME_SelectLoadout.png', region=(0,0,1920,250), grayscale=True, confidence=0.7) != None:
          click(x=950, y=450)
          time.sleep(5)

     if locateOnScreen('./img/MME_InGame.png', region=(730,0,1200,200), grayscale=True, confidence=0.5) != None:
         print("In game waiting...")
         press(random.choice(Random))
         time.sleep(0.5)
    
     if locateOnScreen('./img/MME_EndMatch.png', region=(0,908,1920,1080), grayscale=True, confidence=0.6) != None:
               press('space')
               time.sleep(0.5)
                
    
     if locateOnScreen('./img/leave.PNG', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
               click(x=963, y=623)
               time.sleep(0.5)
     
     if locateOnScreen('./img/space.PNG', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
               press('space')
               time.sleep(0.5)

     
     if locateOnScreen('./img/yes.PNG', region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
               click(x=850, y=713)
               time.sleep(0.5)
               click(x=850, y=713)
         