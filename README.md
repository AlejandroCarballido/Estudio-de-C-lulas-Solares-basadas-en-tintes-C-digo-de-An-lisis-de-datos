En este repositorio se pueden encontrar los archivos utilizados para el análisis de los datos obtenidos de voltaje, intesidad y tiempo de diferentes células solares. 
En total hay tres archivos diferentes que ejecutan tareas distintas:

  -AnalisisCeldas.py: Este script permite generar tablas (en formato Latex) con los diferentes parámetros de una celda solar. Necesitan obtener la información de las curvas I-V que se obtienen con el Sourcemeter. Es necesario cambiar la ruta a la carpeta donde se encuentran los archivos .csv con los datos para generar archivos de texto con Voc e Isc en light y dark, Pmp y FF.

  -transformacionCurvasVtIt.py: Este script permite transformar la información referente al tiempo que se encuentra en los archivos .csv en formato HH:MM:SS y .partial_seconds a un eje de tiempo que comienza en el momento en que se empiezan a tomar los datos. De igual manera es necesario especificar cual es la ruta que lleva a la carpeta con los archivos a analizar.

  -Histogramas.py: Este archivo simplemente crea un histograma si le proporcionas información sobre el número de sucesos.
