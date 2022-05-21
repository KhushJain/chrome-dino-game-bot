from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np
#testing 
restart_coordinates = (480, 503)
dino_coordinates = (207, 534)  
area = (dino_coordinates[0] + 90, dino_coordinates[1], dino_coordinates[0] + 150, dino_coordinates[1] + 5)

def restart():
    pyautogui.click(restart_coordinates)   

def hit():
    pyautogui.keyDown('space')
    time.sleep(0.095)
    pyautogui.keyUp('space')

def detection_area():
    image = ImageGrab.grab(area)
    gray_img = ImageOps.grayscale(image)
    arr = np.array(gray_img.getcolors())
    return arr.mean()

if __name__=="__main__":
    restart()
    while True:
        if detection_area()  < 273:
            hit()