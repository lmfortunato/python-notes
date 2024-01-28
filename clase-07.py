# None -> Asignar un valor vacío o nulo
# Metodos de cadenas
nombre = None

nombre is None #True
nombre == None #True

cadena = "Hola Mundo"
cadena.upper() #"HOLA MUNDO"
cadena.lower() #"hola mundo"
cadena.capitalize() #"Hola mundo"
cadena.title() #"Hola Mundo"
cadena.count("o") #2 -> Le consultas cuantas veces aparece un caracter o subcadena dentro de esa cadena
cadena.find("Mundo") #5 -> Retorna el índice donde se encuentra la subcadena. Si hay más de uno encuentra el primero. Si no encuentra nada retorna un -1
cadena = "Hola Mundo Mundo"
cadena.rfind("Mundo") #11 -> Retorna el índice de la última vez que aparece la subcadena. Si no encuentra nada retorna un -1

cadena.split() #Separa la cadena en una lista de subcadenas y lo retorna en una lista. Si no le paso nada en el () separa por espacios. -> ["Hola", "Mundo", "Mundo"]
cadena3 = "Hola amigo como estas amigo!"
cadena3.split("amigo") # Retorna ["Hola ", "como estas ", "!"] porque amigo es el separador y lo quita
cadena = "Hola Mundo"
",".join(cadena) #Une elementos de una secuencia separados por un separador indicado. En este caso devuelve "H,o,l,a, ,M,u,n,d,o"
" ".join(cadena) # "H o l a  M u n d o"
"||".join(["Pedro", "Juan", "Manuel"]) # 'Pedro||Juan||Manuel'
cadena = "--------Hola mundo -------"
cadena.strip("-") #Elimina el guión medio delante y detrás de la cadena. Queda "Hola mundo". Si no se especifica el carácter elimina los espacios
cadena = "    Hola mundo"
cadena.strip() # "Hola mundo"
cadena.replace("o","a") #Indica qué caracter de la cadena va a ser reemplazado y por cuál. Queda "Hala munda"


# ---------------------------------
# Metodos de listas
lista = [1,2,3,4]
lista.clear() #Elimina todos los elementos de la lista
lista2 = [5,6,7,8]
lista.extend(lista2) #Suma los elementos de una lista con otra. No modifica la lista original
lista.insert(0,0) #Insertas un item en un índice específico. Queda [0,1,2,3,4]
lista.reverse() #Modifica la lista original. Queda [4,3,2,1,0]
lista.sort() #Ordena la lista de menor a mayor. Modifica la lista original
lista.sort(reverse=True) #Ordena la lista de mayor a menor

#Metodos de conjuntos
set1 = {1,2,3}
set2 = {3,4,5}
set1.isdisjoint(set2) #Comprueba si el set1 es distinto al set2, si comparten algún valor similar devuelve false.
# False

set3 = {-1, 99}
set4 = {1,2,3,4,5}
set3.issubset(set4) #Consulta si todos los items del set3 están dentro del otro conjunto.
# False porque no están dentro del set4

set5 = {1,2,3}
set6 = {1,2}
set5.issuperset(set6) #Consulta si contiene todos los items del otro set. El set5 tiene el set 6? Si es así retorna true.

# Metodos que generan un nuevo conjunto
# Copy
set1 = {1,23,4,5}
set2 = set1.copy()

# Union
set1 = {1,2,3}
set2 = {4,5,6}
set1.union(set2)
# {1,2,3,4,5,6} ==> set1 = set1 + set2

# Difference
set1.difference(set2) #Elimina los elementos que son iguales en ambos sets

# Intersection
set1.intersection(set2) #Devuelve un set con los elementos en común entre ambos sets

# Metodos que actualizan el conjunto 

set1 = {1,2,3}
set2 = {3,4,5}
set1.difference_update(set2) #Que tengo de diferente con respecto al set2? Actualiza el set1 con los elementos que sean distintos a los que tiene el set2
# {1,2}
set1.intersection_update(set2)
{3} #Actualiza el set1 con los valores similares al set2

# Metodos de diccionarios
colores = {
    "amarillo" : "yellow",
    "rojo" : "red"
}

colores.get("rojo", "no hay clave rojo") #Busca la clave, si la encuentra devuelve el valor, si no la encuentra devuelve un valor por defecto que le pasamos como segundo parámetrero

colores.keys() #Devuelve una lista con todas las claves del diccionario

colores.values() #Devuelve una lista con todos los valores del diccionario

colores.items() #Devuelve una lista de tuplas con los pares clave:valor
for clave, valor in colores.items():
    print(f"Para la clave {clave}, el valor es: {valor}")
# >>> Para la clave amarillo, el valor es yellow
# >>> Para la clave rojo, el valor es red

