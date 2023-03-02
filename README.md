# Apex Farming Tool for MME/TDM

This Python script automates farming EXP in Apex in the MME/TDM mode. The script uses the PyAutoGUI library to simulate mouse and keyboard clicks.
.

## Usage

### 1. Clone the repository:
    ```sh 
    git clone https://github.com/0xAgartha/ApFarmex
    ```
### 2. Install dependencies:
    ```sh
     sudo apt-get install python3-pip python3-tk python3-dev scrot
    ```
### 3. Install the PyAutoGUI and opencv library: 
    ```sh
    pip install pyautogui opencv-python
    ```
### 4. Enter in script folder:
    ```sh
    cd ApFarmex
    ``` 
### 5. Launch it    
    ```sh
    python3 ApexFarmerMME.py
    ```
### 6. Start the game and don't touch anything more.


## Script Description

The script performs the following actions:

- Clicks on the "Play" button on the home screen
- Closes the news popup window if it appears
- Selects the "TDM" game mode if it is not already selected
- Chooses the MME/TDM mode from the game mode menu
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

