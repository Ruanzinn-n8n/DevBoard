import keyboard

while True:
    if keyboard.press("q"):
        print("Pressionou 'q' !!")
    elif keyboard.press("w"):
        print("Clicou em sair...")
        break
    else:
        continue