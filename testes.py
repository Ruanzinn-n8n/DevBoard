import keyboard
import time

dc = "y"
while dc == "y":
    event = keyboard.read_event()
    name = event.name
    time.sleep(0.5)
    print(name)
    print(type(name))
    dc = input("devo continuar? (y/n)").lower()
    time.sleep(0.2)
    if dc == "y":
        continue
    else:
        break

keyboard.wait("esc")