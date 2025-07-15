cadena1 = "Hola soy Aarón"
cadena2 = "Bienvenido crack!"

# DIR - Devuelve la lista de Atributos Válidos del objeto pasado
print(dir(cadena1))  # ['__add__', '__class__', ..., 'upper', 'zfill']

# UPPER - Convierte en Mayúsculas
print(cadena1.upper())  # "HOLA SOY AARÓN"

# LOWER - Convierte en Minúsculas
print(cadena1.lower())  # "hola soy aarón"

# CAPITALIZE - Primera letra en Mayúscula, el resto en minúscula
print(cadena1.capitalize())  # "Hola soy aarón"

# FIND - Encuentra la primera aparición del valor
print(cadena1.find("soy"))  # 5

# ISNUMERIC - Devuelve True si todos los caracteres son numéricos
print("12345".isnumeric())  # True
print(cadena1.isnumeric())  # False

# ISALPHA - Devuelve True si todos los caracteres son letras (sin espacios)
print("Hola".isalpha())  # True
print(cadena1.isalpha())  # False (por los espacios)

# COUNT - Cuenta cuántas veces aparece un valor
print(cadena1.count("o"))  # 2

# LEN - Devuelve la longitud de la cadena
print(len(cadena1))  # 14

# ENDSWITH - Devuelve True si termina con el valor indicado
print(cadena1.endswith("Aarón"))  # True

# STARTSWITH - Devuelve True si empieza con el valor indicado
print(cadena1.startswith("Hola"))  # True

# REPLACE - Reemplaza una subcadena por otra
print(cadena1.replace("Aarón", "Carlos"))  # "Hola soy Carlos"

# SPLIT - Divide la cadena en una lista por el separador indicado (por defecto espacio)
print(cadena1.split())  # ['Hola', 'soy', 'Aarón']
