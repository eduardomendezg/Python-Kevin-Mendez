from PyQt5.QtWidgets import (QApplication,QMainWindow,QWidget,QLabel,QLineEdit,QPushButton,QMessageBox,QFormLayout,QTextEdit)

import smtplib
import sys
#creamos una clase
class mainVentana (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Envio de correo")
        self.setGeometry(100,100,300,200)

        layout  = QFormLayout()
        self.lbldest = QLabel("Destinatario")
        self.lblasunt = QLabel("Asunto")
        self.lblmensj = QLabel("Mensaje")

        self.editdest = QLineEdit()
        self.editasun = QLineEdit()
        self.editmensj = QTextEdit()
        self.btnenv = QPushButton("Enviar mensaje")
        layout.addRow(self.lbldest,self.editdest)
        layout.addRow(self.lblasunt,self.editasun)
        layout.addRow(self.lblmensj,self.editmensj)
        layout.addRow("",self.btnenv)
        self.setLayout(layout)
        self.btnenv.clicked.connect(self.enviar)
    def enviar(self):
        server = "smtp.gmail.com"
        puerto = 587
        correo = "kevin.mendezgomez.2005@gmail.com"
        contrasena = "jrtc zbvj ofzx rqyp"
        correo2 = "eduardo.mendez.kevin.43@gmail.com"

        #decllarar de funcion para el servidor conexion a servidor
        conex = smtplib.SMTP(server,puerto)

        #print(conex.ehlo())

        conex.starttls()

        conex.login(correo,contrasena)
        conex.login(correo,contrasena)

        #funcion para mandar menssaje
        conex.sendmail(correo,self.editdest.text(),f"Subject: {self.editasun.text()}\n\n" + f"{self.editmensj.toPlainText()}")
        QMessageBox.information(self,"Envio","Enviado correctamente")
        conex.quit()

app = QApplication(sys.argv)   
ventana = mainVentana()
ventana.show()
app.exec() 

    
        