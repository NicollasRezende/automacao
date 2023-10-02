import pyautogui
pyautogui.FAILSAFE = False

minimiza_todas_as_janelas = 'win', 'm'
ponto_inicial = 0, 0
ponto1 = 249, 230
ponto2 = 366, 525
ponto3 = 32, 20

pyautogui.hotkey(minimiza_todas_as_janelas)
pyautogui.rightClick(ponto_inicial)
pyautogui.moveTo(ponto1)
pyautogui.sleep(0.5)
pyautogui.moveTo(ponto2)
pyautogui.click(ponto2)
pyautogui.write('NIKIZIN')
pyautogui.press('enter')
pyautogui.moveTo(ponto3)
pyautogui.doubleClick(ponto3)
pyautogui.sleep(0.5)
pyautogui.write('Nicollas Pereira Rezende')
pyautogui.sleep(0.5)
pyautogui.hotkey('ctrl', 's')
pyautogui.sleep(0.5)
pyautogui.hotkey('alt', 'f4')

# nao faz muita coisa mas mostra que a biblioteca tem um potencial
# enorme pra automatizar coisas
