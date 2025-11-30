# -------------------------------------------------------------
# Ejercicios sobre tipos de datos: Cadenas en Python
# Archivo: ejercicios_cadenas.py
# -------------------------------------------------------------

# 1. Ingrese su nombre y apellido y muestre su nombre completo.
# -------------------------------------------------------------
# Pedimos al usuario que introduzca su nombre y apellido y los mostramos juntos.

nombre = input("Ingrese su nombre: ")        # Solicita el nombre
apellido = input("Ingrese su apellido: ")    # Solicita el apellido

# Concatenamos nombre y apellido con un espacio intermedio y lo mostramos
nombre_completo = nombre + " " + apellido
print("Su nombre completo es:", nombre_completo)

print("-------------------------------------------------------------")

# 2. Ingrese una palabra y muestre cuántas letras tiene.
# -------------------------------------------------------------
# Usamos la función len() para contar el número de caracteres de la palabra.

palabra = input("Ingrese una palabra: ")     # Solicita una palabra
contador = len(palabra)                      # Calcula la cantidad de letras
print("La palabra tiene", contador, "letras.")

print("-------------------------------------------------------------")

# 3. Ingrese una frase y muestre la misma frase en mayúsculas.
# -------------------------------------------------------------
# Para convertir texto a mayúsculas, usamos el método upper().

frase = input("Ingrese una frase: ")         # Solicita una frase
frase_mayus = frase.upper()                  # Convierte toda la frase a mayúsculas
print("Frase en mayúsculas:", frase_mayus)

print("-------------------------------------------------------------")

# 4. Ingrese dos cadenas y muestre cuál es más larga.
# -------------------------------------------------------------
# Comparamos las longitudes de dos textos y mostramos cuál tiene más caracteres.

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

if len(cadena1) > len(cadena2):
    print("La primera cadena es más larga.")
elif len(cadena2) > len(cadena1):
    print("La segunda cadena es más larga.")
else:
    print("Ambas cadenas tienen la misma longitud.")

print("-------------------------------------------------------------")

# 5. Ingrese una palabra y muestre su primera y última letra.
# -------------------------------------------------------------
# Para obtener caracteres específicos usamos los índices: [0] para el primero y [-1] para el último.

palabra2 = input("Ingrese una palabra: ")    # Solicita una palabra
primera_letra = palabra2[0]                  # Obtiene el primer carácter
ultima_letra = palabra2[-1]                  # Obtiene el último carácter

print("La primera letra es:", primera_letra)
print("La última letra es:", ultima_letra)

print("-------------------------------------------------------------")

# Fin del programa
