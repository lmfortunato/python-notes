# Ciclos

# While
numero = 5

while numero > 0:
    print(numero)
    numero -= 1

print(f"Se termina el conteo, número ahora vale {numero}")

# While infinito con un stop
# import time
# numero = 1

# while numero < 10:
#     print(numero)
#     time.sleep(0.5)

# While - else

numero = -1
suma = 0

while numero != 0:
    numero = int(input("Ingresar un número, 0 para salir\n"))
    print("Tu número vale: " + str(numero))

    suma = suma + numero
else:
    print("Has salido con una suma de: " + str(suma))


suma = 0
continuar = True

while continuar == True:
    input_usuario = input("Ingrese un número para la suma o exit para terminar")

    if input_usuario == "exit":
        continuar: False
    else:
        numero = int(input_usuario)
        suma += numero
        print(f"El resultado de la suma es {suma}")

print(f"La suma final es {suma}")

"33".isnumeric()
# True 

# Break detiene la ejecución
i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("Terminó el ciclo while")

# 1
# 2
# 3
# Terminó el ciclo while

# Continue continúa con la iteración salteando la iteración actual

i = 0
while i < 6:
    i += 1
    if i == 3 or i == 5:
        continue
    print(i)

# 1
# 2
# 4
# 6

# For
# Ejemplo 1
estaciones = ["invierno", "verano", "otoño", "primavera"]

for estacion in estaciones:
    print(estacion)

# Ejemplo 2
paises_habitantes = [
    ("Colombia", 50000),
    ("Argentina", 78888),
    ("Peru", 40000),
    ("Brasil", 50000)
]

for tupla in paises_habitantes:
    pais = tupla[0]
    habitantes = tupla[1]
    print(f"El pais {pais} tiene {habitantes} habitantes")

# Enumerate
lenguajes = ["Java", "C", "C++", "Python"]
list(enumerate(lenguajes))
# [(0, "Java"), (1, "C"), (2, "C++"), (3, "Python")]

for indice, lenguaje in enumerate(lenguajes):
    print(f"{indice + 1} {lenguaje}")

# 1 Java
# 2 C
# 3 C++
# 4 Python

# Range
lista_1 = list(range(20)) #Solo le indico el fin
lista_1
# [0, 1, 2, 3, 4, 5, 6, 7, 8, ... 19]

list(range(-2, 11)) #Le indico el principio y el fin
# [-2, -1, 0, 1, 2, 3, 4, ... 10]

list(range(-2, 11, 2)) #Le indico el paso, cada cuanto
# [-2, 0, 2, 4, 6, 8, 10]

for numero in range(1, 20, 3):
    print(numero)
# 1
# 4
# 7
# 10
# 13
# 16
# 19

for numero in range(20, 1, -3): #lo recorre en forma decreciente
    print(numero)
# 20
# 17
# 14
# 11
# 8
# 5
# 2

# For-else
for numero in range(10):
    if numero == 2:
        continue
    print (f"Numero vale {numero}")
else:
    print(f"Se termino de iterar y numero vale: {numero}")