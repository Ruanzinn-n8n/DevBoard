import keyboard
import json

with open("test.json", "r", encoding="utf-8") as arquivo:
    funcoes = json.load(arquivo)
key = funcoes[0]["key"]
short = funcoes[0]["post"]

keyboard.add_hotkey(key, lambda: keyboard.write(short), suppress=True)
keyboard.wait("esc")