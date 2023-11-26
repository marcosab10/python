import ctypes
import keyboard

# Constantes da API do Windows
VK_VOLUME_UP = 0xAF
VK_VOLUME_DOWN = 0xAE

# Flag para verificar se a tecla está atualmente pressionada
volume_up_pressed = False
volume_down_pressed = False

# Função para enviar comando de tecla para o sistema
def press_key(key):
    ctypes.windll.user32.keybd_event(key, 0, 0, 0)

# Função para liberar a tecla
def release_key(key):
    ctypes.windll.user32.keybd_event(key, 0, 2, 0)

# Função para aumentar o volume em 2 unidades
def increase_volume():
    press_key(VK_VOLUME_UP)

# Função para diminuir o volume em 2 unidades
def decrease_volume():
    press_key(VK_VOLUME_DOWN)

# Configuração dos eventos de teclado
keyboard.on_release_key('+', lambda _: release_key(VK_VOLUME_UP))
keyboard.on_press_key('+', lambda _: increase_volume())

keyboard.on_release_key('-', lambda _: release_key(VK_VOLUME_DOWN))
keyboard.on_press_key('-', lambda _: decrease_volume())

# Agora, vamos configurar o evento para parar o programa quando "Shift + E" for pressionado
keyboard.add_hotkey('esc', lambda: keyboard.press_and_release('esc'))

# Mantenha o programa em execução
keyboard.wait('shift + esc')
