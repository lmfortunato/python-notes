# f-string (concatenación)
alumno = input("Nombre del alumno")
nota = int(input("Ingrese la nota"))

f"El alumno {alumno} obtuvo {nota} puntos"

# Listas = Array
mi_lista = [1, 2, 34, 50]

# Concatenar listas
mi_lista + [3, 4, 8]
# >>> [1, 2, 34, 50, 3, 4, 8]

# Reemplazar un valor
mi_lista[2] = 6
# >>> [1, 2, 6, 50]

# Asignación por slicing. Genera una lista nueva, la lista anterior no se modifica
mi_lista = ['a', 'b', 'c', 'd', 'e', 'f']
mi_lista[:3] = ['A', 'B', 'C']
# >>> ['A', 'B', 'C', 'd', 'e', 'f']

# Remover elementos de la lista
mi_lista[:3] = []
# >>> ['d', 'e', 'f']

# Agregar elementos a la lista al final
mi_lista.append(4)

# Eliminar el último elemento de la lista
mi_lista.pop()
mi_lista.pop(3) #Se elimina el elemento de ese índice

# Contar elementos repetidos
numeros = [1,2,1,2,4,1]
numeros.count(1)
# >>> 3

# Conocer el índice de un elemento 
numeros.index(2)
# >>> 1 (Muestra el primer índice donde se encuentra el elemento)

# Tuplas. Listas inmutables
mi_tupla = (1,2,3,4)
mi_tupla_2 = (2,) # Se declara un elemento único con la , para que no lo tome como int

# Tupla vacía
tupla_vacia = ()
tupla_vacia_2 = tuple()

# Sumar tuplas
mi_tupla_nueva = mi_tupla + mi_tupla_2 + ('nuevo valor', 'otro valor')
# mi_tupla_nueva >>> (1,2,3,4,2,'nuevo valor', 'otro valor')

# Desestructuración de listas/tuplas
monto_1, monto_2, monto_3 = (100, 200, 400) # Se le asigna un valor a cada variable
# monto_1 = 100
# monto_2 = 200
# monto_3 = 400

# Anidación. Matriz o lista anidada
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz[0][1] # Devuelve 2

# Modificar una lista dentro de una tupla
tupla = (1, 2, (3, 4), [5, 6])
tupla[-1].append(10)
# tupla = (1 , 2 , (3, 4), [5, 6, 10])

# Transformar listas y tuplas
tupla_edades = (1,2,3)
lista_edades = list(tupla_edades) # >>> [1,2,3]

lista_nombres = ['Lu', 'Juan']
tupla_nombres = tuple(lista_nombres) # >>> ('Lu', 'Juan')