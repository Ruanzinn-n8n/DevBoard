import keyboard

keyboard.add_hotkey("ctrl+alt+f+i", lambda: keyboard.write('for i in :'), suppress=True)
keyboard.add_hotkey('ctrl+alt+p', lambda: keyboard.write('print("")'), suppress=True)
keyboard.add_hotkey("ctrl+alt+k+h", lambda: keyboard.write("keyboard.add_hotkey('ctrl+alt', lambda: keyboard.write(''), suppress=True)"), suppress=True)
keyboard.wait("esc")