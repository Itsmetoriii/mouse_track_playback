from pynput.mouse import Controller
import keyboard
from time import sleep

mouse = Controller()
pos = None

while True:
    if keyboard.is_pressed('ctrl'):
        pos = mouse.position
        print(pos)
        sleep(0.5)
    
    if keyboard.is_pressed('shift'):
        mouse.position = pos

    if keyboard.is_pressed('esc'):
        break

    sleep(0.1)