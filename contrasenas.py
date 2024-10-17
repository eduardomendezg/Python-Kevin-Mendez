import PyPDF2

# Pedir la contraseña al usuario
password = input("Introduce la contraseña: ")

# Abrir el archivo PDF existente
with open("Plan_de_seguridad.pdf", "rb") as archivo:
    # Crear un lector PDF
    lector = PyPDF2.PdfReader(archivo)
    
    # Crear un escritor PDF
    escritor = PyPDF2.PdfWriter()
    
    # Añadir todas las páginas al escritor
    for pagina in range(len(lector.pages)):
        escritor.add_page(lector.pages[pagina])
    
    # Establecer la contraseña
    escritor.encrypt(password)
    
    # Guardar el nuevo archivo PDF con contraseña
    with open("archivo_protegido.pdf", "wb") as archivo_salida:
        escritor.write(archivo_salida)

print("Contraseña añadida al PDF exitosamente.")