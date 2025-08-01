import ctypes
import keyboard
import threading
import pystray
from PIL import Image, ImageDraw

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


# Função para criar um ícone simples
def create_image():
    # Cria uma imagem 64x64 com um círculo azul
    image = Image.new('RGB', (64, 64), color=(255, 255, 255))
    d = ImageDraw.Draw(image)
    d.ellipse((16, 16, 48, 48), fill=(0, 102, 204))
    return image

# Função chamada ao clicar em "Sair" no menu do ícone
def on_quit(icon, item):
    icon.stop()
    # Encerra o programa
    import os
    os._exit(0)

# Função para rodar o ícone da bandeja em uma thread separada
def run_tray():
    icon = pystray.Icon(
        "VolumeControl",
        create_image(),
        "Controle de Volume",
        menu=pystray.Menu(pystray.MenuItem("Sair", on_quit))
    )
    icon.run()

# Inicia o ícone da bandeja em uma thread
threading.Thread(target=run_tray, daemon=True).start()

# Mantenha o programa em execução
keyboard.wait('shift + esc')
