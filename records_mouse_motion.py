from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyListener, Key

running = False  # Control flag
ls = []

def cur_pos(x, y):
    if running:
        print(f"({x}, {y})")
        ls.append((x, y))

def on_key(key):
    global running
    if key == Key.esc:
        print("ESC pressed - Stopping listeners...")
        return False  # Stops the keyboard listener
    elif key == Key.shift:
        print("Shift pressed - Starting mouse tracking...")
        running = True

# Start listeners
mouseListener = MouseListener(on_move=cur_pos)
keyListener = KeyListener(on_press=on_key)

mouseListener.start()
keyListener.start()

keyListener.join()  # Keyboard stops first
mouseListener.stop()  # Then stop the mouse listener

with open("mouse_coords.txt", "w") as file:
    for coord in ls:
        file.write(f"{coord[0]}, {coord[1]}\n")