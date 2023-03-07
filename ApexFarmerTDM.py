from pyautogui import *
import time
import random

random_keys = ['z','q','s','d','4','left','right','down', 'up', '1','2','3','4']
TDM_Mode = 'false'

print("Apex Farming Tool for TDM started")
print("waiting for apex launch")



while True:

     if locateOnScreen('./img/LaunchHomeScreen.png', region=(800,600,1150,750), grayscale=True, confidence=0.7) != None:
          print("Apex found")
          click(x=952, y=717)
          print("HomeScreen skipped")
          time.sleep(5)

     if locateOnScreen('./img/NewsOnStart.png', region=(0,0,1920,100), grayscale=True, confidence=0.7) != None:
          press('esc')
          print("News skipped")
          time.sleep(2)


     if (locateOnScreen('./img/TDM_SelectModeTrios.png', region=(0,700,450,910), grayscale=True, confidence=0.7) and TDM_Mode == 'false') != None:
          time.sleep(1)
          moveTo(240, 820)
          time.sleep(1)
          doubleClick()
          print("Detected Trio: switch incoming")


     if (locateOnScreen('./img/TDM_MenuMode.png', region=(0,0,1920,1080), grayscale=True, confidence=0.7) and TDM_Mode == 'false') != None:
          time.sleep(1)
          moveTo(1020, 580)
          doubleClick()
          time.sleep(1)
          TDM_Mode = 'true'
          print("Select TDM: OK")



     if ((locateOnScreen('./img/ready.png', region=(0,538,447,528), grayscale=True, confidence=0.7) or locateOnScreen('./img/ready2.png', region=(0,538,447,528), grayscale=True, confidence=0.7)) and TDM_Mode == 'true' ) != None:
          print("Preparing for ready")
          moveTo(230, 950)
          click()
          time.sleep(1)
          
     
                
     if (locateOnScreen('./img/cancel_ready.png', region=(0,538,447,528), grayscale=True, confidence=0.7) or locateOnScreen('./img/cancel_ready2.png', region=(0,538,447,528), grayscale=True, confidence=0.7)) != None:
         print("Ready: waiting for game")
         time.sleep(5)
    
     if locateOnScreen('./img/TDM_SelectLoadout.png', region=(0,0,1920,250), grayscale=True, confidence=0.7) != None:
          print("In-game: Loadout Selected")
          click(x=950, y=450)
          time.sleep(5)

     if locateOnScreen('./img/TDM_InGame.png', region=(730,0,1200,200), grayscale=True, confidence=0.5) != None:
         print("In-game: waiting...")
         press(random.choice(random_keys))
         time.sleep(0.5)
    
     if locateOnScreen('./img/TDM_EndMatch.png', region=(0,908,1920,1080), grayscale=True, confidence=0.6) != None:
          press('space')
          time.sleep(0.5)
          print("Game ended: setup for next game")

                
    
     if locateOnScreen('./img/leave.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
          click(x=963, y=623)
          time.sleep(0.5)
          print("Game exited")

     
     if locateOnScreen('./img/space.png', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
          press('space')
          time.sleep(0.5)

     
     if locateOnScreen('./img/yes.png', region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
          click(x=850, y=713)
          time.sleep(0.5)
          click(x=850, y=713)
         