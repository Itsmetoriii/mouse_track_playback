from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyListener, Key
from pynput.mouse import Controller

mouse = Controller()
running = False  # Control flag
ls = []

def cur_pos(x, y):
    
    if running:
        print(f"({x}, {y})")
        ls.append([x, y])

def on_key(key):
    
    global running
    if key == Key.esc:
        print("ESC pressed - Stopping listeners...")
        return False  # Stops the keyboard listener
    elif key == Key.shift:
        print("Shift pressed - Starting mouse tracking...")
        running = True

def on_click(x, y, button, pressed):

    if not pressed:
        return 

    m = len(ls) - 1
    coord = [x, y]
    while m >= 0:
        if ls[m] == coord:
            ls[m].append(True)
            break
        else:
            m -= 1    

    
# Start listeners
mouseListener = MouseListener(on_move=cur_pos)
keyListener = KeyListener(on_press=on_key)
clickListener = MouseListener(on_click=on_click)

clickListener.start()
mouseListener.start()
keyListener.start()

keyListener.join()  # Keyboard stops first
mouseListener.stop()  # Then stop the mouse listener
clickListener.stop()

with open("mouse_coords.txt", "w") as file:
    for coord in ls:
        try:    
            file.write(f"{coord[0]}, {coord[1]}|{coord[2]}\n")
        except IndexError:
            file.write(f"{coord[0]}, {coord[1]}\n")