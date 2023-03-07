# Apex Farming Tool

This Python script automates farming EXP in Apex. The script uses the PyAutoGUI library to simulate mouse and keyboard clicks.

You can choose between 2 modes:

-ApexFarmerTDM.py for Team DeathMatch mode  
-ApexFarmerBR.py for Battle Royale mode

## Usage

####  1. Clone the repository:
    git clone https://github.com/0xAgartha/ApFarmex

#### 2. Install dependencies:
    sudo apt-get install python3-pip python3-tk python3-dev scrot

#### 3. Install the PyAutoGUI and opencv library: 
    pip install pyautogui opencv-python
    
#### 4. Enter in script folder:
    cd ApFarmex
    
#### 5. Launch BR version, start the game and don't touch anything more.  
    python3 ApexFarmerBR.py

#### Or launch TDM version, start the game and don't touch anything more.  
    python3 ApexFarmerTDM.py


## Script Description

The script performs the following actions:
- Click on continue on Apex startup page
- Closes the news popup window if it appears
- Clicks on the "Ready" button and waits for the game to start
- Presses random keys during the game
- Ends the game and goes back to the home screen
- Restart an another game

## Requirements

- Ubuntu
- Python 3.x

## Notes

- The script uses image recognition to locate buttons and menus on the screen. If the images used in the script do not match the images in the game, the script may not work properly.
- Make sure your game is running in fullscreen mode 1920x1080 in english and that the UI is not obstructed by any other windows.
- The script presses random keys during the game. This may not be optimal for gameplay.

## Disclaimer

Please note that using this tool to automate tasks in Apex may be considered cheating and could result in a ban from the game. 
Use at your own risk.

