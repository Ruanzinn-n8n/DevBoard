import keyboard
import functions

keyboard.add_hotkey("del", lambda: functions.colar_text('print("")'), suppress=True)
keyboard.wait("esc")