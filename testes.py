import keyboard
import time

def teste(a):
    print(
        f"nome: {a.name} | "
        f"tipo: {a.event_type} | "
        f"scan: {a.scan_code}"
    )
keyboard.hook(teste)

keyboard.wait("esc")