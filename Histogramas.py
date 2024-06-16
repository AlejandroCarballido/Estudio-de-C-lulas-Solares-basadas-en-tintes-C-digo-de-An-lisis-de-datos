# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:52:25 2024

@author: alcar
"""
import matplotlib.pyplot as plt
import numpy as np

# Datos
data = {
    "Voc Light": [6, 1],
    "Voc Dark": [5, 2],
    "Vph (Light-Dark)": [4, 3],
    "FF": [4, 2],
    "Isc Light": [6, 1],
    "Isc Dark": [5, 2],
    "Iph (Light-Dark)": [7, 0],
    "P": [6, 1]
}

# Configurar fuente a Times New Roman y aumentar el tamaño de las letras y números
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 22  # Tamaño general de la fuente
plt.rcParams['axes.titlesize'] = 24 # Tamaño del título de los ejes
plt.rcParams['axes.labelsize'] = 22  # Tamaño de las etiquetas de los ejes
plt.rcParams['xtick.labelsize'] = 22  # Tamaño de las etiquetas de las marcas del eje x
plt.rcParams['ytick.labelsize'] = 22  # Tamaño de las etiquetas de las marcas del eje y

# Crear figura y ejes con un tamaño más ajustado
fig, axs = plt.subplots(2, 4, figsize=(12, 8), constrained_layout=True, sharey='row')

# Anchura de las barras
bar_width = 0.8

# Primera fila de histogramas
for i, (key, values) in enumerate(data.items()):
    if i < 4:
        axs[0, i].bar(['Nuevo', 'Viejo'], values, color=['blue', 'orange'], width=bar_width)
        axs[0, i].set_title(f"{key}\n") #Nuevo={values[0]}, Viejo={values[1]}
        axs[0, i].set_ylim(0, 8)
        axs[0, i].set_yticks(np.arange(0, 9, 1))

# Segunda fila de histogramas
for i, (key, values) in enumerate(data.items()):
    if i >= 4:
        axs[1, i - 4].bar(['Nuevo', 'Viejo'], values, color=['blue', 'orange'], width=bar_width)
        axs[1, i - 4].set_title(f"{key}\n")#Nuevo={values[0]}, Viejo={values[1]}
        axs[1, i - 4].set_ylim(0, 8)
        axs[1, i - 4].set_yticks(np.arange(0, 9, 1))

# Ocultar etiquetas de eje 'x' y 'y'
for ax in axs.flat:
    ax.label_outer()

# Mostrar figura
plt.show()
