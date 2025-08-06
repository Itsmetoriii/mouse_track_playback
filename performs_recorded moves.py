from pynput.mouse import Controller as MouseController
from pynput.keyboard import Key, Listener
from pynput.mouse import Button
import threading
import pyautogui
import random
from time import sleep

mouse = MouseController()
stop_event = threading.Event()
exit_event = threading.Event()

mouse_motion = []

with open("mouse_coords_1.txt", "r") as file:  # mouse_coords_2 works nicely
    for line in file:
        if "|" in line:
            coord, click = line.strip().split("|")
            x, y = map(int, coord.split(", "))
            mouse_motion.append([x, y, True])
        else:
            if line.strip():
                x, y = map(int, line.split(", "))
                mouse_motion.append([x, y])

if not mouse_motion:
    print("Record some mouse movements")
    exit()
else:
    print("Shift")

start_flag = False

def on_key(key):
    global start_flag
    if key == Key.shift:
        start_flag = True
        return False

def on_key_exit(key):
    if key == Key.esc:
        print("Stopping the program")
        exit_event.set()

with Listener(on_press=on_key) as listener:
    listener.join()

esc_listener = Listener(on_press=on_key_exit)
esc_listener.start()

def move_mouse_with_duration(x, y, duration):
    current_x, current_y = mouse.position
    steps = 100
    sleep_time = duration / steps

    for i in range(steps):
        new_x = current_x + (x - current_x) * (i / steps)
        new_y = current_y + (y - current_y) * (i / steps)
        mouse.position = (int(new_x), int(new_y))
        sleep(sleep_time)

    mouse.position = (x, y)

if start_flag:
    move_mouse_with_duration(mouse_motion[0][0], mouse_motion[0][1], random.uniform(0.5, 0.9))

    for coor in mouse_motion:
        if exit_event.is_set():
            break

        if True in coor:
            mouse.position = (coor[0], coor[1])
            mouse.click(Button.left)
            sleep(random.uniform(0.005, 0.01))
        else:
            mouse.position = coor
            sleep(random.uniform(0.005, 0.01))
