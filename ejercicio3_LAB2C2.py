import matplotlib.pyplot as plt
import pandas as pd
"""
Crear una graficas circular con un dataset: 
Se creo una grafica cicular que muestre el porcentaje de cada tipo de Educacion que hay En Egipto 
Para lo cual solo son 3 tipos de educación en que los estudiantes pueden estar inscritos (IGCSE, IB, Thanweya)

Link: https://www.kaggle.com/datasets/mohamedalabasy/education-in-egypt
"""
#llamamos el archivo CSV
df = pd.read_csv("egypt_education_dataset.csv")
#determinamos la frecuencia de la columna que hemos elegido
frecuencia = df["Education Type"].value_counts()
#creamos la grafica circular y le ponemos el porcentaje
plt.pie(frecuencia.values
        ,labels=frecuencia.index,autopct="%1.1f%%")
#ejecutamos el grafico
plt.show()