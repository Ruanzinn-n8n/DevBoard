import keyboard

keyboard.add_hotkey("del", lambda: keyboard.press("ctrl+c"), suppress=True)
keyboard.add_hotkey("prtscn", lambda: keyboard.press("ctrl+v"), suppress=True)
keyboard.wait("esc")