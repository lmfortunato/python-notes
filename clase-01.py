print("Hello world")

# Integer (int)
4 + 3

# Float
3.21 + 2.15

# Decimal
from decimal import Decimal
Decimal("3.21") + Decimal("2.15")

# División
3/5

# División solo parte entera
15//2

# División resto
7%5

# Multiplicación
2*4

# Potencia 
2**3

# Strings (str)
"Hello world"
'Hello world'

# String con salto de línea y tabulado
"Salto de \nlinea"
"Esto es un \ttabulador"

# String sin formato
print(r"C:\norberto\directorio")

# Texto multilínea
print("""
    una cadena
    otra cadena
""")

# Cita textual
"Messi dijo 'voy a traer la copa'"

# Cadena
"hola" + "mundo"

# Variables
x = 12
x
edad_carlos = 39

# Identificador de la variable
id(x)

# Tipo de dato
type(edad_carlos)

# Entrada del usuario
nombre = input("Ingrese su nombre")

# Pasar de string a entero
int("30")

# Length 
len(edad_carlos)

# Index comienza desde 0
edad_carlos[0]

# Index inverso comienza desde -1
edad_carlos[-1]

# Slicing [inicio:fin:paso] el índice final no se incluye. Paso es cada cuantos caracteres
edad_carlos[0:3]
edad_carlos[3:]
edad_carlos[::-1] #reversa

