#realizamos las importaciones de lo que necesitaremos
from PyQt5.QtWidgets import (QApplication,QWidget, QLineEdit,QVBoxLayout, QPushButton)
import sys 

#creamos una clase llamadda mainwindow donde se creara la ventana
class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
        #ceamos la interfaz
    def UI(self):
        self.setWindowTitle("Clave secreta")
        self.setGeometry(200,200,200,200) #dimensionamos la ventana

        #creamos un diseño para la ventana
        dis = QVBoxLayout()
        #creamos la caja de entrada de texto
        self.clave = QLineEdit()
        self.clave.setEchoMode(QLineEdit.Password)
        #creamos el boton para que imprima en la consola la clave
        btn = QPushButton("Ingregar")
        btn.clicked.connect(self.enviar)
        #agregamos los elementos al diseño
        dis.addWidget(self.clave)
        dis.addWidget(btn)
        self.setLayout(dis)
        #creamos la funcion que recupera e imprime la clave
    def enviar(self):
        claveSecreta = self.clave.text()
        print("Clave secreta introducida: ", claveSecreta)

#creamos la aplicacion
app = QApplication(sys.argv)
ventana = mainWindow()
ventana.show()
app.exec()



