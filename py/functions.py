import keyboard
import pyperclip
import time
import json

def func(text):
    clip_antigo = pyperclip.paste()
    pyperclip.copy(text)
    keyboard.send("ctrl+v")
    time.sleep(0.05)
    pyperclip.copy(clip_antigo)

def cadastrar_tecla(tecla, texto):
    with open("py/config.json", "r", encoding="utf-8") as arq:
        funcoes = json.load(arq)
    new_dic = {
        "key": tecla,
        "post": texto
    }
    funcoes.append(new_dic)
    with open("py/config.json", "w", encoding="utf-8") as arq_2:
        json.dump(funcoes, arq_2, indent=4)

def rodar_terminal():
    print("+===============================+")
    print("|      *    CADASTRAR    *      |")
    print("|===============================|")
    print("| Como deseja cadastrar?        |")
    print("|-------------------------------|")
    print("|  1- Tecla única --> Texto     |")
    print("|  2- Tecla única --> Atalho    |")
    print("|  3- Atalho --> Texto          |")
    print("|  4- Atalho --> Atalho         |")
    print("|  0- Cancelar                  |")
    print("|-------------------------------|")
    print("+===============================+")

    while True:
        escolha = int(input)
        if escolha < 0 or escolha > 4:
            print("Opção inexistente!")
            print("digite novamente.....")
            print("")
        else:
            break
    