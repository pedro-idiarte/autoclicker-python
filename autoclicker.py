import time
import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, Key, Controller as KeyboardController

clicking = False
click_position = None
exit_program = False

mouse = MouseController()
keyboard = KeyboardController()


def set_click_position():
    global click_position
    click_position = mouse.position
    print(f"Posição de clique definida em: {click_position}")

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        print("Autoclick INICIADO. Pressione F6 para pausar.")
    else:
        print("Autoclick PAUSADO. Pressione F6 para retomar.")

def on_press(key):
    global exit_program, clicking, click_position

    try:
        if key == Key.esc:
            exit_program = True
            clicking = False
            print("\nTecla ESC pressionada. Encerrando o programa...")
            return False
        
        if key == Key.f6:
            if not clicking:
                set_click_position()
                toggle_clicking()
            else:
                toggle_clicking()

    except AttributeError:
        pass


def clicker_thread():
    global clicking, click_position, exit_program
    
    print("Thread do clicker iniciada.")
    
    while not exit_program:
        if clicking and click_position:
            mouse.position = click_position
            mouse.click(Button.left, 1)
            time.sleep(0.05) 
        else:
            time.sleep(0.1)
            
    print("Thread do clicker encerrada.")


if __name__ == "__main__":
    print("--- Autoclicker Simples em Python ---")
    print("Instruções:")
    print("1. Posicione o mouse no local desejado para o clique.")
    print("2. Pressione a tecla F6 para definir a posição e INICIAR o autoclick.")
    print("3. Pressione F6 novamente para PAUSAR o autoclick.")
    print("4. Pressione a tecla ESC a qualquer momento para ENCERRAR o programa.")
    print("--------------------------------------")

    click_thread = threading.Thread(target=clicker_thread)
    click_thread.start()

    with Listener(on_press=on_press) as listener:
        listener.join()

    click_thread.join()
    
    print("Programa finalizado.")
