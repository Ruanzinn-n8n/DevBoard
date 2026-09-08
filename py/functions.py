import keyboard
import pyperclip
import time

def colar_text(text):
    clip_antigo = pyperclip.paste()
    pyperclip.copy(text)
    keyboard.send("ctrl+v")
    time.sleep(0.05)
    pyperclip.copy(clip_antigo)