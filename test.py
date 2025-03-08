from pynput.keyboard import Key, Controller
import keyboard
from time import sleep
import random

typer = Controller()
ls = [list('hello world'), list('I am not an idiot')]
counter = 0

while True:

    if keyboard.is_pressed('esc'):
        break

    if keyboard.is_pressed('shift'):
        for i in range(len(ls[counter])):
            typer.type(ls[counter][i])
            sleep(random.uniform(0.150, 0.155))

            sleep(0.1)
        if counter == len(ls) - 1:
            pass
        else:
            counter += 1
    
    sleep(0.01)