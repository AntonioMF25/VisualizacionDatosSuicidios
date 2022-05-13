# ------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import os

# ------------------------------------------------------------------------------------

df, df2 = pd.read_csv("files/data.csv"), pd.read_csv("files/population.csv")
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
pais_suicidios, pais_poblacion = {}, {}

for country in sorted(pd.unique(df["country"])):
    pais_suicidios[country] = 0

for indice, fila in df2.iterrows():
    pais_poblacion[fila["country"]] = fila["population"]

for indice, fila in df.iterrows():
    if not pd.isnull(fila["suicides_no"]):
        pais_suicidios[fila["country"]] = int(pais_suicidios.get(fila["country"]) + fila["suicides_no"])

numSuicidios = []
for indice, fila in world.iterrows():
    if fila["name"] in pais_suicidios.keys():
        numSuicidios.append(pais_suicidios.get(fila["name"]) / pais_poblacion.get(fila["name"]))
    else:
        numSuicidios.append(None)

world.insert(6, "suicides_no", numSuicidios, True)
fig, ax = plt.subplots()
ax.set_title("Suicidios entre 1979 y 2016")
ax.set_xlabel("Longitud")
ax.set_ylabel("Latitud")

#cmap="OrRd"
world.plot(column="suicides_no", cmap="plasma", ax=ax, zorder=5, legend=True,
    missing_kwds=dict(color = "lightgrey",))
fig.savefig("%s\\files\\grafica2.png" % os.path.abspath(os.curdir), dpi=fig.dpi)
plt.show()

# ------------------------------------------------------------------------------------
