from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
import time
import pyautogui


def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mouse = MouseController()
    keyboard = KeyboardController()
    position = ()
    counter = 0
    while(True):
        if counter == 0:
            position = (20,0,0,0)
        elif counter == 1:
            position = (0, 20, 0, 0)
        elif counter == 2:
            position = (0, 0, -20, 0)
        elif counter == 3:
            position = (0, 0, 0, 20)
        keyboard.press('n')
        print("something")
        time.sleep(1200)
        print("something")
        keyboard.release('n')
        pyautogui.moveRel(position)
        mouse.click(Button.left, 1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
