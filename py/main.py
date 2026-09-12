import keyboard
import functions
import time
import json
import threading

def carregar_atalhos():

    try:
        with open("py/config.json", "r", encoding="utf-8") as arquivo:
            funcoes = json.load(arquivo)

        for i in funcoes:
            tecla = i["key"]
            text = i["post"]
            keyboard.add_hotkey(tecla, lambda t=text: functions.func(t), suppress=True)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Arquivo config.json não encontrado. Criando uma nova estrutura...")
        with open("py/config.json", "w") as arquivo:
            json.dump([], arquivo)

def rodar_terminal():
    print("+===============================+")
    print("|      *    CADASTRAR    *      |")
    print("|===============================|")
    print("| Como deseja cadastrar?        |")
    print("|-------------------------------|")
    print("|  1- Key --> Text / Shortcut   |")
    print("|  2- Shortcut --> Text         |")
    print("|  3- REMAP                     |")
    print("|  4- Remove shortcut           |")
    print("|  0- Cancel                    |")
    print("|-------------------------------|")
    print("+===============================+")
    print('  ------#OBS: O atalho deve seguir o seguinte formato: "key1+key2"')
    print("")

    while True:
        print("Escolha uma opção:")
        try:
            escolha = int(input())
            if 0 <= escolha <= 4:
                break
            print("Opção inexistente!")
            print("digite novamente.....")
            print("")
        except ValueError:
            print("Digite apenas um número entre 0 e 4!\n")

    match escolha:
        case 1:
            print("Aguarde...")
            key = functions.leitura_tecla()
            print("Aguarde...")
            time.sleep(1)
            print("")
            print("Digite o texto / atalho:")
            text = input()
            functions.cadastrar_tecla(key, text)
            keyboard.add_hotkey(key, lambda t=text: functions.func(t), suppress=True)

        case 2:
            print("Digite o atalho:")
            key = input()
            print("Digite o texto:")
            text = input()
            functions.cadastrar_tecla(key, text)
            keyboard.add_hotkey(key, lambda t=text: functions.func(t), suppress=True)

        case 3:
            print("Aguarde...")
            key_1 = functions.leitura_tecla()
            print("")
            print("Aguarde...")
            key_2 = functions.leitura_tecla()
            print("Quase lá...")
            time.sleep(1)
            print("")
            functions.cadastrar_tecla(key_1, key_2)
            keyboard.add_hotkey(key_1, lambda t=key_2: keyboard.send(t), suppress=True)

        case 4:
            print("Aguarde...")
            time.sleep(1)
            i = functions.remove_short()
            print(f"Short [{i}] removido com sucesso!")

        case 0:
            print("Cadastro cancelado...")
            time.sleep(1)
            print("Até mais!")

    if escolha != 0 and escolha != 4:
        print("Cadastro concluido com sucesso!")
    if escolha == 4:
        print("Atalho removido com sucesso!")    

def abrir_em_t():
    t = threading.Thread(target=rodar_terminal)
    t.start()

carregar_atalhos()

keyboard.add_hotkey("ctrl+shift+k", abrir_em_t, suppress=True)

print("======================================================================")
print("===  SISTEMA INICIADO  ===============================================")
print("=== Pressione [Ctrl + Shift + K] a qualquer momento para abrir o menu ")
print("=== Pressione [ESC] para encerrar o programa.")
print("======================================================================")
keyboard.wait("esc")

