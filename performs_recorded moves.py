from pynput.mouse import Controller
from time import sleep
from pynput.keyboard import Key, Listener
from pynput.mouse import Button
import random
import time

mouse = Controller()
mouse_motion = []

with open("mouse_coords.txt", "r") as file:
    for line in file:

        if "|" in line:
            coord, click = line.strip().split("|")
            x, y = map(int, coord.split(", "))
            click = click.strip()
            click = True
            mouse_motion.append([x, y, click])
        else:
            
            if line == "\n":
                continue
            else:    
                x, y = map(int, line.split(", "))
                mouse_motion.append([x, y])
        

if mouse_motion == []:
    print("Record some mouse movements")
    exit()

mouse = Controller()
start_flag = False

def on_key(key):
    global start_flag
    if key == Key.shift:
        start_flag = True
        return False

with Listener(on_press=on_key) as listener:
    listener.join()


#this part is not at all important just moving the mouse to the place where the ls[0] is
def move_mouse_with_duration(x, y, duration):  # Duration in seconds
    current_x, current_y = mouse.position
    steps = 100  # More steps = smoother movement
    sleep_time = duration / steps

    for i in range(steps):
        new_x = current_x + (x - current_x) * (i / steps)
        new_y = current_y + (y - current_y) * (i / steps)
        
        mouse.position = (int(new_x), int(new_y))
        time.sleep(sleep_time)

    mouse.position = (x, y)



if start_flag:

    move_mouse_with_duration(mouse_motion[0][0],mouse_motion[0][1] ,random.uniform(0.5, 0.9))

    for coor in mouse_motion:
        
        if True in coor:
            mouse.position = (coor[0], coor[1])
            mouse.click(Button.left)
            sleep(random.uniform(0.005, 0.01))
        else:
            mouse.position = coor
            sleep(random.uniform(0.005, 0.01))
        