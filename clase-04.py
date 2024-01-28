# Condicionales
edad = 30
if edad >= 18:
    print("Es mayor")
else:
    print("No es mayor")

comando = "Salir"

if comando == "Entrar":
    print("Bienvenido")
elif comando == "Saludo":
    print("Hola!")
elif comando == "Salir":
    print("Adiós")
else:
    print("Comando inválido")

# Condicionales anidados

x = 5

if x > 10:
    print("Por encima de 10!")
    if x > 20:
        print("También por encima de 20!")
    else:
        print("Pero no por encima de 20")
else:
    print("Es menos que 10 :( ")

# Ternario
edad = 25
es_mayor_de_edad = ""

if edad >= 18:
    es_mayor_de_edad = "mayor"
else:
    es_mayor_de_edad = "menor"

# >>>>> ternario

es_mayor_de_edad = "mayor" if edad >= 18 else "menor"

