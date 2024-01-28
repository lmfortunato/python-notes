# Programación orientada a objetos
# 49.45
class Persona:
    #Método constructor, construye objetos de esta clase
    def __init__(self, nombre, edad):
        # Todo lo que definamos en _init_ se corre al crear una instancia de la clase
        self.nombre = nombre
        self.edad = edad
    #El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método

persona_1 = Persona(nombre="Luis", edad=29)

print(persona_1.nombre)