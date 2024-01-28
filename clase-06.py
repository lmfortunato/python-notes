# Conjuntos / set -> Colección mutable y no ordenada de objetos únicos. No se puede consultar el índice ni hacer slicing
conjunto = {1, 2, 3, 4}
otro_conjunto = {"Hola", "como", "estas", "?"}
conjunto_vacio = set()

import random
# Generamos 50 numeros random del 1 al 1000
random_numbers = random.sample(range(1, 1001), 50)

# Convert the random numbers to a set to remove duplicates
random_numbers = set(random_numbers)

print(random_numbers)

# Crear un set a partir de una lista o tupla
conjunto_c = set(["Emanuel", "Ivan", "Diego", "Pedro", "Emanuel"]) #Elimina duplicados y lo convierte en un set desordenado

conjunto_c.add(5) #Agrega un elemento al conjunto

conjunto_c.update([5, 6, 7, 8]) #Agrega varios elementos dentro del conjunto

len(conjunto_c) #Conocer la longitud del conjunto

conjunto_c.discard(6) #Elemento a eliminar del set. Si no existe se ignora, no da error
# {5, 7, 8}

conjunto_c.remove(7) #Igual que el discard, pero da error si no existe
#{5, 6, 8}

2 in conjunto_c #False
5 in conjunto_c #True

conjunto_c.clear() #Vacía el conjunto

conjunto_c.pop() #Remueve y retorna un elemento aleatorio del set

# Diccionarios -> Colección mutable y ordenada de objetos
diccionario = {} #Diccionario/objeto vacío
colores = {
    "amarillo" : "yellow",
    "azul" : "blue",
    "rojo" : "red"
}

type(colores) #"dict"

colores["amarillo"] # -> "yellow" consulto el valor de la clave
colores["amarillo"] = "amarelo" #Reasigno el valor de la clave
colores["verde"] = "green" #Agrego un nuevo par clave:valor al objeto

colores.update({"amarillo":"white", "naranja":"orange"}) #Actualiza el valor de la clave amarillo y agrega el nuevo par clave:valor

len(colores) #Longitud del objeto
del colores["azul"] #Elimina el par clave:valor. Si no existe se ignora

"amarillo" in colores 
# True

"blue" in colores 
# False
# Sirve con las claves, no valores

"blue" in colores.values()
# True

colores.clear() #Elimina todos los valores del objeto
colores = {} #También vacía el objeto

if not "violeta" in colores:
    colores["violeta"] = "purple"

colores2 = {
    "gris" : "gray",
    "rosa" : "pink"
}

colores.update(colores2) #Agrego al diccionario anterior un nuevo diccionario

