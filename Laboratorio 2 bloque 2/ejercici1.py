import matplotlib as plt
import pandas as pd 

df = pd.read_csv("laptop_prices.csv")

frec = df["Product"].value_counts()
plt.bar(frec.index,frec.values)
plt.show(); 