import keyboard

keyboard.add_hotkey("ctrl+f+i", lambda: keyboard.write('for i in :'), suppress=True)
keyboard.wait("esc")