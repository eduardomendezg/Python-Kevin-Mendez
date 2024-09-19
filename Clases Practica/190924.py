#jrtc zbvj ofzx rqyp
import smtplib
#valores necesarios para smtplib
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
conex.sendmail(correo,correo2,"Subject: Asunto del "+ "mensaje\n\n Este es el cuerpo")

conex.quit()
