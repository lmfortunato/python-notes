# Excepciones
# Try-Except
# Ejemplo 1
a = 7
b = "hola"

try:
    print("Entrando en el try")
    print(a + b)
    print("Terminando el try")
except:
    print("Ha ocurrido un error al sumar")

print("Termino la ejecucion")

# Ejemplo 2
while True:
    try:
        a = float(input("Introduce un número: "))
        b = float(input("Introduce otro número: "))
        print("Ingresaste bien los dos numeros")
        suma = a + b
        break
    except:
        print("Ha ocurrido un error. Tienes que introducir dos números, inténtalo nuevamente")

print(f"La suma es {suma}")

# Ejemplo 3 con finally
while True:
    try:
        a = float(input("Introduce un número: "))
        b = float(input("Introduce otro número: "))
        print("Ingresaste bien los dos numeros")
        suma = a + b
    except:
        print("Ha ocurrido un error. Tienes que introducir dos números, inténtalo nuevamente")
    else:
        # Se ejecuta si el bloque try no arrojó errores
        print("La suma se ha realizado correctamente")
        print(f"La suma es {suma}")
        break
    finally:
        # Esto se ejecuta siempre, inclusive después de un break
        # Se usa para acciones de limpieza
        print("Finally, para limpieza")

# Ejemplo 4. Excepciones por tipo
def ejemplo_division():
    constante = 5
    try:
        num = float(input("Introduce un número divisor: "))
        cociente = constante/num
        print(cociente)
    except ValueError as err:
        print("No se puede dividir el número entre una cadena vacía o un texto")
        print(f"Mensaje de error devuelto por Python: {err}")
    except ZeroDivisionError as err:
        print("No se puede dividir por cero, prueba otro número")
    except Exception as err:
        # Nos sirve para capturar errores no previstos. Comodín
        print("Ha ocurrido un error no previsto", type(err)._name_)
        print(f"El error fue {err}")

ejemplo_division()

# Ejemplo 5. Excepción con raise. Forzamos el error pero detenemos la ejecución, mostrando el mensaje de error
def ejemplo_division():
    constante = 5
    try:
        num = float(input("Introduce un número divisor: "))
        cociente = constante/num
        print(cociente)
    except ValueError as err:
        print("No se puede dividir el número entre una cadena vacía o un texto")
        print(f"Mensaje de error devuelto por Python: {err}")
        raise
    except ZeroDivisionError as err:
        print("No se puede dividir por cero, prueba otro número")
        raise
    except Exception as err:
        # Nos sirve para capturar errores no previstos. Comodín
        print("Ha ocurrido un error no previsto", type(err)._name_)
        print(f"El error fue {err}")
        raise

ejemplo_division()

# Ejemplo 6
base_datos = {
    "pedro":"12345",
    "paco":"contra"
}

def chequear_credenciales(username, password, base_datos):
    password_en_mi_db = base_datos[username]
    if password_en_mi_db == password:
        return True #La contraseña es correcta
    else:
        # Contraseña incorrecta. Disparo error con raise
        raise ErrorAutenticacion("Username or password don't match")

chequear_credenciales("pedro", "1244", base_datos)