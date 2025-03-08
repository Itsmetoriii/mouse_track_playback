import pyautogui
import time

timer = 1

while True:
    try:
        if loc := pyautogui.locateCenterOnScreen('search_bar_locater.png'):    
            x, y = loc
            y -= 500
            pyautogui.moveTo(x, y, duration=1)
            #pyautogui.click()
            break
    except Exception:
        print("Not detected")
        time.sleep(timer)