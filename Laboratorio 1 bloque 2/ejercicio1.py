#importamos las librerias que necesitamos
from PyQt5.QtWidgets import (QApplication, QMainWindow)
import sys 
from PyQt5 import uic
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #llamamos al documento ui donde tenemos la interfaz
        uic.loadUi("UI/ejercicio1.ui", self)
app = QApplication(sys.argv)
ventana = mainWindow()
ventana.show()
app.exec()