# class Perro:
#     pass #Es para evitar un error cuando todavía no tenemos código dentro

class Perro:
    especie = "Mamifero" #Atributos de clase, se aplican para todos los objetos por igual
    superpoder = "Dar amor" #Se puede usar como valor por defecto y más adelante cambiarlo

    #Método constructor / método mágico
    def __init__(self, nombre, raza):
        #atributos de instancia
        self.nombre = nombre
        self.raza = raza

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, raza: {self.raza}, especie: {self.especie}"

    #Métodos personalizados
    def ladrar(self):
        return f"{self.nombre} acaba de ladrar"
    
    def correr(self, km: int):
        return f"{self.nombre} está corriendo {km} kilómetros"



#Creo los objetos
perro1 = Perro(nombre = "Paco", raza = "Labrador")
perro2 = Perro("India", "Bulldog")

print(perro1.raza)
print(perro2.nombre)
print(perro2.especie) #mamifero
print(perro2.superpoder) # "Dar amor"
perro2.superpoder = "Perro bombero" #Sobreescribo el valor por defecto
print(perro2.superpoder) #Perro bombero
print(perro1.superpoder) #Dar amor
perro1.comida_favorita = "Croquetas de pollo" #Agrego un atributo que no estaba definido en la clase
print(perro1.comida_favorita)
print(f"Atributo por atributo {perro1.nombre}, {perro1.raza}, {perro1.especie}, {perro1.superpoder}, {perro1.comida_favorita}")
print(perro1) #Va a buscar el atributo str que le creé
print(perro1.ladrar())
print(perro1.correr(5))

# Métodos mágicos
# __init__
# __str__ -> imprime el objeto de manera human readable
# __len__ -> obtener el numero de elementos que tenga el objeto
# __getitem__ ->
# __setitem__ ->

class Vector: 
    # Constructor
    def __init__(self, data, titulo):
        self._data = data #atributo privado, el dev no recomienda acceder a él externamente
        self.titulo = titulo

    # Devuelve los valores del objeto como string
    def __str__(self) -> str:
        return f"Vector cuyos valores son {self._data}"
    
    # Muestra la longitud del objeto
    def __len__(self):
        return len(self._data)
    
    # Devuelve el objeto guardado en una posicion del data
    def __getitem__(self, pos):
        return self._data[pos]
    
    # Permite sobreescribir un objeto en una posicion dada del data
    def __setitem__(self, pos, value):
        self._data[pos] = value

    # Permite iterar
    def __iter__(self):
        for pos in range(0, len(self._data)):
            yield self._data[pos]

    #Lógica adicional
    def calcular_product(self):
        return "Calculando el producto"
    
    def agregar(self, elem):
        self._data.append(elem)


vector_1 = Vector(data = [1,2], titulo = "titulo 1")

print(vector_1._data) # [1,2]
print(vector_1.__len__()) #2
print(len(vector_1)) # Es lo mismo que el anterior pero más amigable visiblemente

print(vector_1.__str__()) #Vector cuyos valores son [1, 2]
print(vector_1) #Es lo mismo que lo de arriba, python entiende que un print llama al metodo str de un objeto

print(vector_1.__getitem__(1)) # 2
print(vector_1[1]) # Hace lo mismo que el get item

vector_1.__setitem__(1, 10) # Sobreescribo en la posición 1 el valor por 10
print(f"estoy imprimiendo el nuevo valor con __setitem__, es: {vector_1}")
vector_1[1] = 20 #Es lo mismo que el anterior
print(f"imprimo el nuevo valor, esta vez así vector_1[1] = 20, me queda: {vector_1}")

vector_1.agregar(200) # Hace un append. Me queda [1, 20, 200]
print(f"ahora le agrego un nuevo valor con el método agregar, me queda: {vector_1}")

#Clases anidadas
class Trabajador:
    class Departamentos: #Esta clase se usa por lo general para definir unas constantes
        VENTAS = 'ventas'  #Al declararlo en mayúsculas le indicas que es un valor que no debería cambiar
        GERENCIA = 'gerencia'
        MANTENIMIENTO = 'mantenimiento'

    def __init__(self, nombre, apellido, departamento):
        self.nombre = nombre
        self.apellido = apellido
        self.departamento = departamento

print(Trabajador.Departamentos.VENTAS)
trabajador = Trabajador("Juan", "Gomez", departamento=Trabajador.Departamentos.VENTAS)
print(trabajador.nombre)
print(trabajador.departamento)

#Encapsulamiento 
# se utiliza para que los atributos o metodos internos de una clase no se puedan acceder ni modificar desde afuera, si no con un metodo 
class Persona:
    #atributos de clase
    tipo = "humano"
    __sueldo = 2000 #Es un atributo protegido o "encapsulado"

    def __init__(self, nombre, apellido):
        #atributos de instancia
        self.nombre = nombre #Dato publico
        self.__apellido = apellido #Dato encapsulado
        self._nacionalidad = "ciudadano del mundo" #Dato que por convencion el dev sugiere que sea privado, pero py no lo protege

    def __obten_carta_astral(self): #método encapsulado
        return"Tendras un futuro brillante... o tal vez no"

    def hablar(self):
        return "bla bla bla"
    
persona1 = Persona("Pedro", "Rojas")
print(f"tipo: {persona1.tipo}")
print(f"nombre: {persona1.nombre}")
print(f"hablar: {persona1.hablar()}")
print(persona1._nacionalidad)
print(f"apellido: {persona1.__apellido}") #Devuelve error, has no attribute '__apellido' porque esta encapsulado
print(f"Carta astral: {persona1.__obten_carta_astral()}") 

# Name mangling _Clase__metodo
# Se puede acceder a los atributos encapsulados
print(f"Ahora con name mangling: \n apellido: {persona1._Persona__apellido}")
print(f"Ahora con name mangling: \n carta astral: {persona1._Persona__obten_carta_astral()}")

#manera correcta de encapsular
class Jugador:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    #Se generan metodos get publicos para acceder a los atributos encapsulados
    #metodos getters
    def get_nombre(self):
        return self.__nombre #Dentro del codigo si puedo acceder al atributo encapsulado
    
    def get_apellido(self):
        return self.__apellido
    
    #Se generan metodos set publicos para modificar los valores de los atributos encapsulados
    #metodos setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

jugador1 = Jugador("Brenda", "Benitez")

jugador1.get_nombre()
jugador1.get_apellido()

jugador1.set_nombre("Julia")
jugador1.set_apellido("Britez")

