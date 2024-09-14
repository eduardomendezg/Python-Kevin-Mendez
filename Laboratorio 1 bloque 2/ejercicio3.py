#importamos las librerias que necesitaremos 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
#creamos la clase ventana donde realizaremos el procedimiento
class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.UI()
    #creamos la funcion para diseñar la ventana 
    def UI(self):
        self.setWindowTitle("Cédula y Nombre Completo")
        self.setGeometry(400, 400, 200, 200)

        dis = QVBoxLayout()
        #creamos las etiquetas y las entradas de texto
        lbl_cedula = QLabel("Número de Cédula:")
        self.intro_cedula = QLineEdit()

        lbl_nombre = QLabel("Nombre Completo:")
        self.intro_nombre = QLineEdit()

        btn_enviar = QPushButton("Ingresar")
        btn_enviar.clicked.connect(self.enviar_informacion)
        #agregamos los elementos al diseño
        dis.addWidget(lbl_cedula)
        dis.addWidget(self.intro_cedula)
        dis.addWidget(lbl_nombre)
        dis.addWidget(self.intro_nombre)
        dis.addWidget(btn_enviar)

        self.setLayout(dis)
    #recuperamos la informacion y la imprimimos
    def enviar_informacion(self):
        cedula = self.intro_cedula.text()
        nombre_completo = self.intro_nombre.text()
        print("Cédula:", cedula)
        print("Nombre Completo:", nombre_completo)

#ejecutamos la aplicacion 
app = QApplication(sys.argv)
ventana = Ventana()
ventana.show()
sys.exit(app.exec_())

