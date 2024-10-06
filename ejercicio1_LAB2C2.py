#importamos las librerias necesarias
import matplotlib.pyplot as plt
import pandas as pd
""" Crear una grafica de barras en la cual se use una dataset de kaggle:
Se hizo uso de una dataset en la cual obtiene un analisis de los precios de laptop,
para lo cual se hizo una grafica de barrras en la cual represente un top de 10 empresas y que se muestre 
la distibución de precios por empresas. 

Link del dataset: https://www.kaggle.com/datasets/owm4096/laptop-prices
 """
#leemos el dataset
df = pd.read_csv("laptop_prices.csv")
#se tomaran solo los valores del top de las primeras 10 empresas 
fr = df["Company"].value_counts().nlargest(10)
#se edita el tamaño del grafico para mayor visualización.
plt.figure(figsize=(100,6))
#se crea el grafico de barras de acuerdo a los datos del dataset, se escribren los encabezados y
# se muestran los datos
plt.bar(fr.index,fr.values)
plt.xlabel('Empresa')
plt.ylabel('Cantidad')
plt.title('Distribución de precios por empresa')
plt.show()