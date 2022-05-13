# ------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import os

# ------------------------------------------------------------------------------------

df = pd.read_csv("files/data.csv")
df = df.sort_values("year")

xTotal = sorted([year for year in pd.unique(df["year"])])
yTotal = [0 for numero in range(38)]
for indice, fila in df.iterrows():
    if not pd.isnull(fila["suicides_no"]):
        yTotal[int(fila["year"]) - 1979] += int(fila["suicides_no"])

xHombres = sorted([year for year in pd.unique(df["year"])])
yHombres = [0 for numero in range(38)]
for indice, fila in df.iterrows():
    if not pd.isnull(fila["suicides_no"]) and fila["sex"] == "male":
        yHombres[int(fila["year"]) - 1979] += int(fila["suicides_no"])

xMujeres = sorted([year for year in pd.unique(df["year"])])
yMujeres = [0 for numero in range(38)]
for indice, fila in df.iterrows():
    if not pd.isnull(fila["suicides_no"]) and fila["sex"] == "female":
        yMujeres[int(fila["year"]) - 1979] += int(fila["suicides_no"])

fig, ax = plt.subplots()
ax.plot(xTotal, yTotal, color="red", label="Total")
ax.plot(xHombres, yHombres, color="blue", label="Hombres")
ax.plot(xMujeres, yMujeres, color="green", label="Mujeres")

plt.title("Suicidios entre 1979 y 2016")
plt.xlabel("Años (1979-2016)")
plt.ylabel("Número de suicidios")
plt.legend(loc="upper left")
fig.savefig("%s\\files\\grafica1.png" % os.path.abspath(os.curdir), dpi=fig.dpi)
plt.show()

# ------------------------------------------------------------------------------------
