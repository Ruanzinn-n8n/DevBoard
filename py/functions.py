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
    print("|  1- Tecla --> Texto / Atalho  |")
    print("|  2- Atalho --> Texto          |")
    print("|  3- REMAP                     |")
    print("|  0- Cancelar                  |")
    print("|-------------------------------|")
    print("+===============================+")
    print('  ------#OBS: O atalho deve seguir o seguinte formato: "key1+key2"')
    print("")

    while True:
        print("Escolha uma opção:")
        escolha = int(input())
        if escolha < 0 or escolha > 3:
            print("Opção inexistente!")
            print("digite novamente.....")
            print("")
        else:
            break

    match escolha:
        case 1:
            print("Digite a tecla:")
            event = keyboard.read_event()
            key = event.name
            time.sleep(0.5)
            print(f"Tecla identificada: {key}!")
            print("Aguarde...")
            time.sleep(1)
            print("")
            print("Digite o texto / atalho:")
            text = input()
            cadastrar_tecla(key, text)

        case 2:
            print("Digite o atalho:")
            key = input()
            print("Digite o texto:")
            text = input()
            cadastrar_tecla(key, text)

        case 3:
            print("Digite a tecla 1:")
            event = keyboard.read_event()
            key_1 = event.name
            time.sleep(0.5)
            print(f"Tecla identificada: {key_1}!")
            print("Aguarde...")
            time.sleep(1)
            print("")
            print("Digite a tecla 2:")
            event = keyboard.read_event()
            key_2 = event.name
            time.sleep(0.5)
            print(f"Tecla identificada: {key_2}!")
            print("Aguarde...")
            time.sleep(1)
            print("")
            cadastrar_tecla(key_1, key_2)

        case 0:
            print("Cadastro cancelado...")
            time.sleep(1)
            print("Até mais!")

    if escolha != 0:
        print("Cadastro concluido com sucesso!")
    print("---- Clique ESC para sair")
    keyboard.wait("esc")