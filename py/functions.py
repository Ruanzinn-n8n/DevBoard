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

def leitura_tecla():
    print(">>>> Digite a tecla:")
    time.sleep(0.5)
    while True:
        event = keyboard.read_event(suppress=False)
        if event.event_type == "down":
            chave = event.name
            print(f"Tecla identificada: [{chave}]!")
            time.sleep(0.2)
            break
    return chave

def remove_short():
    time.sleep(0.5)
    with open("py/config.json", "r", encoding="utf-8") as arq:
        funcoes = json.load(arq)
    print("=====================================")
    print("= Shortcuts - - - - - - - - - - - - -")
    print("=-----------------------------------=")
    for i in range(len(funcoes)):
        ch = funcoes[i]["key"]
        fc = funcoes[i]["post"]
        print(f"= {i+1} - [{ch}] --> [{fc}]")
    print("====================================")
    while True:
        try:
            opc = int(input("Digite o número do atalho:\n"))
            if 0 <= opc <= len(funcoes):
                break
            else:
                print(f"Digite um número entre 0 e {len(funcoes)}!")
        except ValueError:
            print("Apenas números...")
    i = opc -1
    with open("py/config.json", "w", encoding="utf-8") as arquivo:
        rem = json.load(arquivo)
    removido = rem.pop(i)
    return ch
