# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 19:22:46 2024

@author: alcar
"""
import os
import csv

def adjust_fractional_seconds(data):
    # Inicializar variables
    adjusted_data = []
    initial_value = float(data[0])
    previous_value = initial_value
    seconds_offset = 0

    for value in data:
        current_value = float(value)
        # Chequear si los fractional seconds han pasado de .9... a .0...
        if current_value < previous_value:
            seconds_offset += 1

        # Calcular la diferencia ajustada
        adjusted_time = (seconds_offset + current_value) - initial_value
        adjusted_data.append(adjusted_time)
        previous_value = current_value

    return adjusted_data

def process_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            process_file(file_path)

def process_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        lines = list(reader)

    # Los datos empiezan en la décima fila
    header = lines[7]
    data_lines = lines[8:]

    # Extraer la última columna (Fractional Seconds)
    fractional_seconds = [line[-1] for line in data_lines]

    # Ajustar los valores de fractional seconds
    adjusted_times = adjust_fractional_seconds(fractional_seconds)

    # Crear un nuevo archivo con los tiempos ajustados
    new_filename = file_path.replace(".csv", "_fixed.csv")
    with open(new_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for i, line in enumerate(data_lines):
            new_line = line[:-1] + [adjusted_times[i]]
            writer.writerow(new_line)

# Especificar el directorio que contiene los archivos CSV
directory_path = './curvas'

# Procesar todos los archivos en el directorio
process_files_in_directory(directory_path)
