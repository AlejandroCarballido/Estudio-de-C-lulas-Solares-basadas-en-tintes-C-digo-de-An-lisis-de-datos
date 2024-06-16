# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:47:35 2024

@author: alcar
"""
import pandas as pd
import glob
import os

# Función para procesar un archivo y calcular los valores requeridos
def procesar_archivo(file_path):
    data = pd.read_csv(file_path, sep='\t')

    # Extraer columnas necesarias para condiciones de luz
    intensidad_light = data['IL']
    voltaje_light = data['VL']

    # Extraer columnas necesarias para condiciones de oscuridad
    intensidad_dark = data['ID']
    voltaje_dark = data['VD']

    # Calcular Voc (voltaje cuando la corriente es cero) para luz y oscuridad
    try:
        Voc_light = voltaje_light[intensidad_light.abs().idxmin()]
    except:
        Voc_light = float('nan')
    
    try:
        Voc_dark = voltaje_dark[intensidad_dark.abs().idxmin()]
    except:
        Voc_dark = float('nan')

    # Calcular Isc (corriente cuando el voltaje es cero) para luz y oscuridad
    try:
        Isc_light = intensidad_light[voltaje_light.abs().idxmin()]
    except:
        Isc_light = float('nan')
    
    try:
        Isc_dark = intensidad_dark[voltaje_dark.abs().idxmin()]
    except:
        Isc_dark = float('nan')

    # Filtrar datos entre Voc y V=0 para luz
    if not pd.isna(Voc_light):
        if Voc_light >= 0:
            filtro_light = (voltaje_light <= Voc_light) & (voltaje_light >= 0)
        else:
            filtro_light = (voltaje_light >= Voc_light) & (voltaje_light <= 0)
        intensidad_light_filtrada = intensidad_light[filtro_light]
        voltaje_light_filtrado = voltaje_light[filtro_light]
    else:
        intensidad_light_filtrada = pd.Series(dtype=float)
        voltaje_light_filtrado = pd.Series(dtype=float)

    # Calcular la potencia P = I * V para los valores filtrados en luz
    if not intensidad_light_filtrada.empty and not voltaje_light_filtrado.empty:
        potencia_light_filtrada = intensidad_light_filtrada * voltaje_light_filtrado
        # Encontrar la máxima potencia Pmp en valor absoluto
        Pmp = potencia_light_filtrada.abs().max()
    else:
        Pmp = float('nan')

    # Calcular el factor de forma FF = Pmp / (Voc_light * Isc_light)
    if not pd.isna(Pmp) and not pd.isna(Voc_light) and not pd.isna(Isc_light) and Voc_light != 0 and Isc_light != 0:
        FF = abs(Pmp / (Voc_light * Isc_light))
    else:
        FF = float('nan')

    # Convertir los valores a microvoltios, nanoamperios y picovatios
    Voc_light *= 1e6 # microvoltios
    Isc_light *= 1e9  # nanoamperios
    Voc_dark *= 1e6  # microvoltios
    Isc_dark *= 1e9  # nanoamperios
    Pmp *= 1e12  # picovatios

    return Voc_light, Voc_dark, Isc_light, Isc_dark, Pmp, FF, potencia_light_filtrada

# Directorio con los archivos TSV (ruta relativa)
reference_name='grafito2'
folder_path = './'+reference_name  # Nombre de la carpeta en la que están los archivos
file_paths = glob.glob(os.path.join(folder_path, '*.txt'))

# Lista para almacenar los resultados
resultados = []

# Procesar cada archivo en la carpeta
for file_path in file_paths:
    file_name = os.path.basename(file_path)
    Voc_light, Voc_dark, Isc_light, Isc_dark, Pmp, FF, potencia_light_filtrada = procesar_archivo(file_path)
    resultados.append((file_name, Voc_light, Voc_dark, Isc_light, Isc_dark, Pmp, FF))

# Generar la tabla en formato LaTeX
latex_table = """
\\begin{table}[h!]
\\centering
\\caption{Resultados de mediciones}
\\begin{tabular}{llcccccc}
\\hline
Referencia && \multicolumn{2}{c}{Voc (\SI{}{\micro\volt})} & \multicolumn{2}{c}{Isc (nA)} & Pmp (pW) & FF \\\\
&& Light & Dark & Light & Dark & & \\\\
\\hline
"""

for resultado in resultados:
    file_name, Voc_light, Voc_dark, Isc_light, Isc_dark, Pmp, FF = resultado
    latex_table += f"{file_name} && {Voc_light:.2f} & {Voc_dark:.2f} & {Isc_light:.2f} & {Isc_dark:.2f} & {Pmp:.2f} & {FF:.3f} \\\\\n"

latex_table += """
\\hline
\\end{tabular}

\\label{tab: resultados}
\\end{table}
"""

# Guardar la tabla LaTeX en un archivo
write_in=reference_name+'.txt'
with open(write_in, 'w') as f:
    f.write(latex_table)

print(f"La tabla LaTeX ha sido guardada en {write_in}")

