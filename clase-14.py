#Herencias
class Animal:
    planeta = "Tierra"
    esta_vivo = True

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"
    
    def hablar(self):
        return "Este es el metodo hablar"
    
    def moverse(self):
        return "Este es el metodo moverse"
    
    def describir(self):
        return f"Soy un animal del tipo: {type(self).__name__}"


class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} hace Guau!"
    
    def moverse(self):
        return f"{self.nombre} ha caminado con 4 patas"
    
    def dar_pata(self):
        return f"{self.nombre} te ha dado la pata"


class Abeja(Animal):
    def hablar(self):
        return "Bzzz"
    
    def moverse(self):
        return "Volando"
    
    def picar(self):
        return "Picar!"


jirafa = Animal("Josefa", 25)

perro = Perro("Pocho", 5)

print(perro)
print(perro.hablar())
print(perro.dar_pata())
print(perro.planeta)

abeja = Abeja("Marta", 1)
print(abeja.picar())
print(abeja.hablar())


# Super -> llama al constructor del ancestro y le puede agregar nuevos atributos

class Gato(Animal):
    def __init__(self, nombre, edad, raza, duenio):
        #Llamamos al constructor del ancestro
        super().__init__(nombre, edad)
        self.raza = raza
        self.duenio = duenio
    
    def hablar(self):
        return "Miau"
    
    def moverse(self):
        #Llamamos al metodo de la class Animal
        resultado = super().moverse()
        return f"{resultado} y caminando en 4 patas"
    

gato = Gato("Regina", 2, "siames", "Pedro")

print(gato.moverse())
print(gato.duenio)
print(gato.hablar())

#Herencia múltiple. Más de un ancestro
class ClaseX:
    pass

class Clase1(ClaseX):
    def metodo_a(self):
        return "A: soy de la clase 1"
    
    def metodo_b(self):
        return "B: soy de la clase 1"
    
    def metodo_c(self):
        return "C: soy de la clase 1"
    
class Clase2:
    def metodo_a(self):
        return "A: soy de la clase 2"
    
    def metodo_b(self):
        return "B: soy de la clase 2"
    
    def metodo_d(self):
        return "D: soy de la clase 2"
    
class Clase3(Clase1, Clase2):
    def metodo_a(self):
        return "A: soy de la clase 3"
    
    def saludar(self):
        return "Hola"
    
# Me fijo el orden de prioridad de las clases heredadas
print(Clase3.__mro__) #(<class '__main__.Clase3'>, <class '__main__.Clase1'>, <class '__main__.ClaseX'>, <class '__main__.Clase2'>, <class 'object'>)

ejemplo = Clase3()

print(ejemplo.metodo_a()) #Devuelve "A: soy de la clase 3"
print(ejemplo.metodo_b()) #Devuelve "B: soy de la clase 1" porque tiene prioridad
print(ejemplo.metodo_c()) #"C: soy de la clase 1"
print(ejemplo.metodo_d())#return "D: soy de la clase 2"

print(dir(ejemplo)) #Para chequear los metodos mágicos de la clase object

#EL SUPER() SE COMPORTA SIGUIENDO EL ORDEN DEL MRO

class Mamifero:
    def hablar(self):
        return "Habla un mamifero"
    

class Felino:
    def hablar(self):
        return "Habla un felino"
    
class Gato2(Felino, Mamifero):
    def hablar(self):
        #return super().hablar() #Toma el metodo de felino, porque es al que llama primero
        return Mamifero.hablar(self) #Para que tome el otro metodo se invoca a la clase. Se puede invocar a cualquier metodo de cualquier clase, no hace falta que sea ancestro
    

print(Gato2.__mro__)
gato2 = Gato2()
print(gato2.hablar())

# Duck Typing. El tipo de objeto no es relevante si no sus metodos
class Pato:
    def hablar(self):
        return 'Cuac cuac!'

class Vaca:
    def hablar(self):
        return 'Muuu'

class Gato3:
    def hablar(self):
        return 'Miauu'
    
pato = Pato()
vaca = Vaca()
gato = Gato3()

pato.hablar() #Cuac cuac!

lista_animales = [pato, vaca, gato]

for animal in lista_animales:
    print(animal.hablar())

#Polimorfismo -> Duck typing + herencia. Un método puede comportarse distinto en cada hijo. Se sobreescribe

class Animal:

    def hablar(self):
        return 'Hablo'


class Perro(Animal):

    def hablar(self):
        return "Guau Guau"


class Gallo(Animal):

    def hablar(self):
        return "Kikiriki"
    

#Chequear ancestros
isinstance(perro, Perro) # true