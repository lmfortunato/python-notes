# Funciones
def saludar(nombre):
    saludo = f"Hola {nombre}, como estas?"
    return saludo

saludar("Ana")
print(saludar("Ana"))

def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

sumar(15, 18)

def ejemplo_retorno_multiple():
    return "hola", 10, 2.5, [3,4,5]

ejemplo_retorno_multiple()
# Retorna una tupla con todos los valores. ("hola", 10, 2.5, [3,4,5])

# Desestructuración de tuplas
var_1, var_2, var_3, var4 = ejemplo_retorno_multiple()
# var_1 = "hola"
# var_2 = 10
# var_3 = 2.5
# var_4 = [3,4,5]

