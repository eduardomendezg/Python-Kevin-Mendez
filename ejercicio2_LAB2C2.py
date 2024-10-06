#importamos las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
"""
Hacer una grafica de lineas de un dataset:
Se hizo un grafico de lineas que muestra las horas estudiadas y el porcentaje de clases asistidas para 
mostrar estos dos factores que afectan el rendimientos de los estudiantes
Link: https://www.kaggle.com/datasets/lainguyn123/student-performance-factors 
"""
# llamamos archivo CSV
df = pd.read_csv('StudentPerformanceFactors.csv')

# Seleccionamos las columnas
columnas = [ 'Hours_Studied','Attendance']
#dimencionamos el grafico
plt.figure(figsize=(10, 6))
#creamos un bucle que recorra las columnas y las muestre en el grafico de lineas
for col in columnas:
    plt.plot(df[col], label=col)
#ponemos los encabezados y los titulos
plt.xlabel('Numero de horas estudiadas y porcentajes de clases asistidas')
plt.ylabel('Horas estudiadas y clases asistidas')
plt.title('Horas estudiadas y porcentaje de clases')
#agrego las leyendas
plt.legend()
#ejecuto el grafico
plt.show()