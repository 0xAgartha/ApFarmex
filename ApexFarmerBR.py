from pyautogui import *
import time
import random

random_keys = ['z','q','s','d','4','left','right','down', 'up', '1','2','3','4']
team_filled = False

print("Apex Farming Tool for BR is started")
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

     if locateOnScreen('./img/FillTeam_Empty.png', region=(3,520,445,304), grayscale=True, confidence=0.9) != None:
          print("Fill Team: changing")
          moveTo(70, 680)
          click()
          time.sleep(1)
     
     if locateOnScreen('./img/FillTeam.png', region=(3,520,445,304), grayscale=True, confidence=0.9) != None:
          team_filled = True
          print("Fill Team: OK")

     if ((locateOnScreen('./img/ready.png', region=(0,538,447,528), grayscale=True, confidence=0.7) or locateOnScreen('./img/ready2.png', region=(0,538,447,528), grayscale=True, confidence=0.7)) and team_filled == True) != None:
          time.sleep(1)
          print("Preparing for ready")
          moveTo(230, 950)
          click()
          time.sleep(1)
     
                
     if (locateOnScreen('./img/cancel_ready.png', region=(0,538,447,528), grayscale=True, confidence=0.7) or locateOnScreen('./img/cancel_ready2.png', region=(0,538,447,528), grayscale=True, confidence=0.7)) != None:
         print("Ready: waiting for game")
         time.sleep(5)
    
    
     if locateOnScreen('./img/InGame.png', region=(87,755,379,304), grayscale=True, confidence=0.5) != None:
         print("In-game: waiting...")
         press(random.choice(random_keys))
         time.sleep(1)
    
     if locateOnScreen('./img/dead.png', region=(441,19,1017,304), grayscale=True, confidence=0.6) != None:
               print("Game ended: setup for next game")
               click(1771, 1040)
               time.sleep(0.5)
               click(1771, 1040)
               time.sleep(0.5)
               press('space')
               time.sleep(0.5)


     if locateOnScreen('./img/leave.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
               click(963, 623)
               time.sleep(0.5)
               print("Game exited")

     
     if locateOnScreen('./img/space.png', region=(676,777,619,304), grayscale=True, confidence=0.6) != None:
               press('space')
               time.sleep(0.5)

     
     if locateOnScreen('./img/yes.png', region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
               click(850, 713)
               time.sleep(0.5)
               click(850, 713)


     
