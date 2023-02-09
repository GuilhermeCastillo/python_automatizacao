# !python3
# mouseNow.py - Exibe a posição atual do cursor do mouse
import pyautogui
print('Press Ctrl + C to quit')
# TODO: obtém e exibe as coordenadas do mouse
try:
    while True:
        # TODO: Obtém e exibe as coordenadas do mouse
        x, y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + 'Y' + str(y).rjust(4)
        print(positionStr, end="")
        print('\b' * len(positionStr), end="", flush=True)
except KeyboardInterrupt:
    print('\nDone.')
