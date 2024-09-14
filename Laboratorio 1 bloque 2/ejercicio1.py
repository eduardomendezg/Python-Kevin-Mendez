from PyQt5.QtWidgets import (QApplication, QMainWindow,QWidget, QLineEdit,QFormLayout,QLabel)
import sys 
from PyQt5 import uic
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/ejercicio1.ui", self)
app = QApplication(sys.argv)
ventana = mainWindow()
ventana.show()
app.exec()