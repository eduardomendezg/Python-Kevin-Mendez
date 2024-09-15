#importamos las librerias necesarias para este ejercicio
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QWidget,QVBoxLayout,QHBoxLayout, QPushButton, QLineEdit,QLabel)

#creamos una clase donde crearemos el funcionamiento y el proceso
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        #Dimencionamos la pantalla 
        self.setGeometry(300, 300, 300, 350)
        self.setWindowTitle('Datos de Mascotas')

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        #creamos las entradas de datos de todas la información que necesitamos 
        mascota1_layout = QHBoxLayout()
        mascota1_layout.addWidget(QLabel('Nombre Mascota 1:'))
        self.mascota1_nombre = QLineEdit()
        mascota1_layout.addWidget(self.mascota1_nombre)
        mascota1_layout.addWidget(QLabel('Edad Mascota 1:'))
        self.mascota1_edad = QLineEdit()
        mascota1_layout.addWidget(self.mascota1_edad)
        mascota1_layout.addWidget(QLabel('Raza Mascota 1:'))
        self.mascota1_raza = QLineEdit()
        mascota1_layout.addWidget(self.mascota1_raza)
        layout.addLayout(mascota1_layout)

        mascota2_layout = QHBoxLayout()
        mascota2_layout.addWidget(QLabel('Nombre Mascota 2:'))
        self.mascota2_nombre = QLineEdit()
        mascota2_layout.addWidget(self.mascota2_nombre)
        mascota2_layout.addWidget(QLabel('Edad Mascota 2:'))
        self.mascota2_edad = QLineEdit()
        mascota2_layout.addWidget(self.mascota2_edad)
        mascota2_layout.addWidget(QLabel('Raza Mascota 2:'))
        self.mascota2_raza = QLineEdit()
        mascota2_layout.addWidget(self.mascota2_raza)
        layout.addLayout(mascota2_layout)

        mascota3_layout = QHBoxLayout()
        mascota3_layout.addWidget(QLabel('Nombre Mascota 3:'))
        self.mascota3_nombre = QLineEdit()
        mascota3_layout.addWidget(self.mascota3_nombre)
        mascota3_layout.addWidget(QLabel('Edad Mascota 3:'))
        self.mascota3_edad = QLineEdit()
        mascota3_layout.addWidget(self.mascota3_edad)
        mascota3_layout.addWidget(QLabel('Raza Mascota 3:'))
        self.mascota3_raza = QLineEdit()
        mascota3_layout.addWidget(self.mascota3_raza)
        layout.addLayout(mascota3_layout)

        #imprimimos los datos 
        self.boton_imprimir = QPushButton('Imprimir')
        layout.addWidget(self.boton_imprimir)
        self.boton_imprimir.clicked.connect(self.imprimir_datos)
    #creamos una funcion para imprimir los datos 
    def imprimir_datos(self):
        print('Datos de las mascotas:')
        print(f'Mascota 1: {self.mascota1_nombre.text()}, {self.mascota1_edad.text()}, {self.mascota1_raza.text()}')
        print(f'Mascota 2: {self.mascota2_nombre.text()}, {self.mascota2_edad.text()}, {self.mascota2_raza.text()}')
        print(f'Mascota 3: {self.mascota3_nombre.text()}, {self.mascota3_edad.text()}, {self.mascota3_raza.text()}')

#creaos y ejecutamos la aplicación
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()