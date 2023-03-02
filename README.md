# Apex Farming Tool for MME/TDM

This Python script automates farming EXP in Apex in the MME/TDM mode. The script uses the PyAutoGUI library to simulate mouse and keyboard clicks.


## Usage

####  1. Clone the repository:
    git clone https://github.com/0xAgartha/ApFarmex

#### 2. Install dependencies:
     sudo apt-get install python3-pip python3-tk python3-dev scrot

#### 3. Install the PyAutoGUI and opencv library: 
    pip install pyautogui opencv-python
    
#### 4. Enter in script folder:
    cd ApFarmex
    
#### 5. Launch it, start the game and don't touch anything more.    
    python3 ApexFarmerMME.py

## Script Description

The script performs the following actions:
- Click on continue on Apex startup page
- Closes the news popup window if it appears
- Chooses the MME/TDM mode from the game mode menu if it is not already selected
- Clicks on the "Ready" button and waits for the game to start
- Selects a loadout for the game
- Presses random keys during the game
- Ends the game and goes back to the home screen
- Restart an another game

## Requirements

- Ubuntu
- Python 3.x

## Notes

- The script uses image recognition to locate buttons and menus on the screen. If the images used in the script do not match the images in the game, the script may not work properly.
- Make sure your game is running in fullscreen mode 1920x1080 in english and that the UI is not obstructed by any other windows.
- The script presses random keys during the game. This may not be optimal for gameplay, and it is recommended to modify the script to press specific keys instead.

## Disclaimer

Please note that using this tool to automate tasks in Apex may be considered cheating and could result in a ban from the game. 
Use at your own risk.

