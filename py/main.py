import keyboard
import functions
import json

with open("py/config.json", "r", encoding="utf-8") as arquivo:
    funcoes = json.load(arquivo)

for i in funcoes:
    tecla = i["key"]
    text = i["post"]
    keyboard.add_hotkey(tecla, lambda t=text: functions.func(t), suppress=True)

keyboard.wait("esc")

layr e viado