# -------------------------------------------------------------
# Ejercicios sobre tipos de datos: Carácter en Python
# Archivo: ejercicios_caracteres.py
# -------------------------------------------------------------

print("=== EJERCICIOS DE CARÁCTER ===")

# 1. Ingrese una letra y determine si es vocal o consonante.
# -------------------------------------------------------------
# Las vocales son: a,e,i,o,u (mayúsculas y minúsculas)
print("\n1. VOCAL O CONSONANTE")
letra = input("Ingrese una letra: ").lower().strip()  # Convertimos a minúscula y quitamos espacios

if len(letra) == 1 and letra in "aeiou":
    print("La letra", letra, "es una VOCAL.")
else:
    print("La letra", letra, "es una CONSONANTE (o no es una letra válida).")

print("-------------------------------------------------------------")

# 2. Ingrese un carácter y determine si es mayúscula o minúscula.
# -------------------------------------------------------------
# Usamos isupper() para mayúsculas e islower() para minúsculas
print("\n2. MAYÚSCULA O MINÚSCULA")
caracter = input("Ingrese un carácter: ").strip()

if len(caracter) == 1:
    if caracter.isupper():
        print("El carácter", caracter, "es MAYÚSCULA.")
    elif caracter.islower():
        print("El carácter", caracter, "es MINÚSCULA.")
    else:
        print("El carácter", caracter, "no es letra.")
else:
    print("Por favor ingrese SOLO un carácter.")

print("-------------------------------------------------------------")

# 3. Ingrese un carácter y muestre su código ASCII.
# -------------------------------------------------------------
# Usamos ord() para obtener el valor ASCII de un carácter
print("\n3. CÓDIGO ASCII")
caracter_ascii = input("Ingrese un carácter: ")

if len(caracter_ascii) == 1:
    codigo = ord(caracter_ascii)  # Convierte carácter a su código ASCII
    print("El código ASCII de", caracter_ascii, "es:", codigo)
else:
    print("Por favor ingrese SOLO un carácter.")

print("-------------------------------------------------------------")

# 4. Ingrese una letra y conviértala a mayúscula.
# -------------------------------------------------------------
# Usamos upper() para convertir a mayúscula
print("\n4. CONVERTIR A MAYÚSCULA")
letra_convertir = input("Ingrese una letra: ")

if len(letra_convertir) == 1:
    letra_mayus = letra_convertir.upper()  # Convierte a mayúscula
    print("La letra convertida a mayúscula es:", letra_mayus)
else:
    print("Por favor ingrese SOLO una letra.")

print("-------------------------------------------------------------")

# 5. Ingrese un carácter y determine si es un número.
# -------------------------------------------------------------
# Usamos isdigit() para verificar si es un dígito (0-9)
print("\n5. ¿ES NÚMERO?")
caracter_numero = input("Ingrese un carácter: ")

if len(caracter_numero) == 1:
    if caracter_numero.isdigit():
        print("El carácter", caracter_numero, "ES un NÚMERO (dígito).")
    else:
        print("El carácter", caracter_numero, "NO es un número.")
else:
    print("Por favor ingrese SOLO un carácter.")

print("-------------------------------------------------------------")
print("=== FIN DE LOS EJERCICIOS ===")
