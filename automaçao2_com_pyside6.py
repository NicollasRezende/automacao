import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget
import pyautogui


class Janela(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Executar', self)
        self.btn.clicked.connect(self.automate_task)

        self.resize(200, 100)
        self.setWindowTitle('Automatização')
        self.show()

    def automate_task(self):
        pyautogui.FAILSAFE = False
        minimiza_todas_as_janelas = 'win', 'm'
        ponto_inicial2 = 711, 380
        ponto_inicial = 0, 0
        ponto1 = 249, 229
        ponto2 = 366, 530
        ponto3 = 32, 20
        pyautogui.moveTo(ponto_inicial2)
        pyautogui.sleep(0.5)
        pyautogui.click(ponto_inicial2)
        pyautogui.sleep(0.5)
        pyautogui.click(ponto_inicial2)
        pyautogui.sleep(0.5)
        pyautogui.hotkey(minimiza_todas_as_janelas)
        pyautogui.sleep(0.5)
        pyautogui.hotkey(minimiza_todas_as_janelas)
        pyautogui.sleep(0.5)
        pyautogui.rightClick(ponto_inicial)
        pyautogui.sleep(0.5)
        pyautogui.moveTo(ponto1)
        pyautogui.sleep(0.5)
        pyautogui.click(ponto1)
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
        pyautogui.hotkey('alt', 'f4')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Janela()
    sys.exit(app.exec())
