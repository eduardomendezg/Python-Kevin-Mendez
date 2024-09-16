
#importamos las librerias que necesitamos
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.UI()

    def UI(self):
        self.setGeometry(300, 300, 300, 350)
        self.setWindowTitle('Datos de Persona')

        dis = QVBoxLayout()
        self.setLayout(dis)
        #cremoas una lista con los datos caracteristicos y el tipo de entrada
        datos = [
            ('Nombre', QLineEdit()),
            ('Apellido', QLineEdit()),
            ('Edad', QLineEdit()),
            ('Género', QLineEdit()),
            ('Dirección', QLineEdit()),
            ('Teléfono', QLineEdit()),
            ('Correo electrónico', QLineEdit()),
            ('Ocupación', QLineEdit()),
            ('Nivel de estudios', QLineEdit()),
            ('Hobbies', QLineEdit())
        ]
        #recorremos los datos y los agregamos al diseño para que se muestren en pantalla
        for lbl, field in datos:
            dis.addWidget(QLabel(lbl))
            dis.addWidget(field)

        # guardamos la informacion
        button = QPushButton('Guardar')
        dis.addWidget(button)
        button.clicked.connect(self.guardarDatos)
        #creamos una funcion ara guardar los datos
    def guardarDatos(self):
        datos = {}
        for i, (lbl, field) in enumerate(datos):
            datos[lbl] = field.text()

        # Imprimir los datos en la consola
        print('Datos personales:')
        for k, v in datos.items():
            print(f'{k}: {v}')
#ejecutamos la aplicacion 
app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec_()