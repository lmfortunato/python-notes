# Chequear si una variable es un numero
variable = 4

isinstance(variable, int)
variable.isnumeric()

# Funciones lambda. Funciones pequeñas anonimas. 
# lambda parámetros : retorno
lambda a,b : a + b

sumar_lambda = lambda a, b : a + b

sumar_lambda(20, 5)

def restar (a, b):
    return a - b

restar(20, 15)

# Otra opción es llamar a los argumentos por nombre
restar(a = 15, b = 12)

restar(b = 12, a = 15) # No importa el orden si le pones el nombre

# Funciones con parámetros por defecto
def saludar_alumno(alumno="estudiante"):
    return f"Bienvenido {alumno}"

saludar_alumno() #al no pasarle ningún valor devuelve "estudiante"
saludar_alumno("Ramiro") #Toma el valor que le estoy pasando


lista = [10, 50, 100]

def multiplicar(numeros):
    for indice, numero in enumerate(numeros):
        # Multiplico cada elemento por 2
        numeros[indice] = numero*2
    return numeros

list(enumerate(lista))
# Devuelve una lista de tuplas
#[(0, 10), (1, 50), (2, 100)]

multiplicar(lista)
# Devuelve [20, 100, 200]

print(lista)
# La lista se modificó, ahora vale lo mismo que al ejecutarse la función

# Si no quiero que se vea modificado el valor original de la lista le paso una copia

lista_2 = [30, 40, 50]

# Opcion 1
multiplicar(lista_2[:])

# Opcion 2
multiplicar(lista_2.copy())

# Argumentos indeterminados
# Args -> arguments
# kwargs -> keyword arguments. Captura todos los argumentos pasados por nombre que no fueron definidos en los parametros de la funcion

def suma(*args): #Le puedo pasar la cantidad de argumentos que quiera, se pasa como una tupla
    return sum(args)

suma(5,5,3)
suma(4,3,5,6,7,7)

def imprimir_argumentos(**kwargs): #Se pasa como diccionario
    for key, value in kwargs.items():
        print(f"{key} = {value}")

imprimir_argumentos(nombre = "Juan", apellido = "Perez")

# Ejemplo
def obtener_promedio(notas):
    return sum(notas) / len(notas)

def obtener_promedio_alumno(alumno, **kwargs):
    promedio = obtener_promedio(**kwargs)
    texto = f"Hola {alumno}, tu promedio es {promedio}"
    return texto

obtener_promedio_alumno(alumno = "Juan", notas = [10, 10, 6])

# Recursividad -> La funcion se llama a si misma
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
factorial(5)

# factorial de 5 es = 5 * 4!
# 5! = 1 * 2 * 3 * 4 * 5
# 4! = 1 * 2 * 3 * 4
# 3! = 1 * 2 * 3
# 2! = 1 * 2
# 1! = 1

# Ejemplo 2
def cuenta_regresiva(n):
    print(f"Funcion llamada con argumento {n}")
    if n == 0:
        print("Despegue!")
    else:
        print(f"inicio del bloque {n}")
        cuenta_regresiva(n - 1)
        print(f"Fin del bloque: {n}")

cuenta_regresiva(5)

# >>> cuenta_regresiva(5)
# Funcion llamada con argumento 5
# inicio del bloque 5
# Funcion llamada con argumento 4
# inicio del bloque 4
# Funcion llamada con argumento 3
# inicio del bloque 3
# Funcion llamada con argumento 2
# inicio del bloque 2
# Funcion llamada con argumento 1
# inicio del bloque 1
# Funcion llamada con argumento 0
# Despegue!
# Fin del bloque: 1
# Fin del bloque: 2
# Fin del bloque: 3
# Fin del bloque: 4
# Fin del bloque: 5
# >>>