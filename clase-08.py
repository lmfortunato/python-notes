# Creo el nombre del archivo
nombre_archivo = "archivo.txt"
# Abro un archivo existente o creo uno nuevo, la "w" significa write.
archivo = open(nombre_archivo, "w")
# Escribo en el documento
archivo.write("Esto es un texto nuevo, nueva linea")
# Guardo y cierro el documento
archivo.close()

# -------------------------------
nombre = "Pedro"
apellido = "Rojas"
dni = 111

persona = {
    "Nombre":nombre,
    "Apellido": apellido,
    "Dni": dni
}

nombre_archivo_2 = "archivo2.txt"
archivo = open(nombre_archivo_2, "a") #La "a" es de append, es decir que va a agregarlo en lugar de sobreescribirlo
archivo.write(f'{persona["Nombre"]}, {persona["Apellido"]}, {persona["Dni"]}\n')
archivo.close()

# Leer archivos
f = open(nombre_archivo_2, "r")
# Ahora el "r" va a hacer referencia a read
content = f.read()
print(content)
f.close()

f = open(nombre_archivo_2, "r")
lines = f.readlines() #Ahora cada línea del txt me la va a devolver como una lista de renglones
print(lines)
f.close()

f = open(nombre_archivo_2, "r") #Abro el archivo
f.seek(4) #Le indico desde que número de caracter debe comenzar a leer. Le muevo el cursor
print(f.read()) #Lee e imprime
f.close() #Cierra

# ------------ JSON
# Importo la libreria json
import json
# Indico el nombre del archivo
ruta_json = "persona.json"
# Abro el archivo en write
archivo = open(ruta_json, "w")
# Vuelco el diccionario en un json, donde el primer parámetro va a ser el diccionario, el segundo la ruta del archivo y el tercero el indentado
json.dump(persona, archivo, indent=4)
archivo.close()

# Para simplificar el open y close usamos el with, que puede servir para todos los tipos de archivos
import json
ruta_json = "persona.json"
with open(ruta_json, "w") as archivo:
    json.dump(persona, archivo, indent=4)


# Leer el archivo json
with open(ruta_json, "r") as archivo_read:
    data_json = json.load(archivo_read)

print(f'el archivo json es {data_json}')

# CSV
import pandas as pd
import numpy as np

ruta_dataset = "archivo.csv"

lector_csv = pd.read_csv(ruta_dataset)

type(lector_csv)
# >> pandas.core.frame.DataFrame
lector_csv.head(3) #Muestra las primeras tres filas de la tabla
lector_csv.tail() #Muestra las ultimas cinco filas
lector_csv.sample(3) #Muestra tres registros al azar
lector_csv["sede"] #Te muestra los datos de la columna indicada
lector_csv["sede"].value_counts() #Te devuelve la cantidad de registros de un mismo valor que haya en esa columna
lector_csv[lector_csv["sede"] == "Parque Chacabuco"] #Filtro por la columna "sede", los registros que tengan el valor "Parque Chacabuco"
