# ============================
# USO DE INPUT EN PYTHON
# ============================

# INPUT BÁSICO - Captura texto del usuario
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)

# CONVERSIÓN A ENTERO - Captura número y lo convierte
edad = int(input("¿Cuántos años tienes? "))
print("Tendrás", edad + 1, "el año que viene")

# CONVERSIÓN A FLOAT - Para decimales
altura = float(input("¿Cuál es tu altura en metros? "))
print("Tu altura es:", altura, "m")

# BOOLEANO DESDE TEXTO (sí/no)
respuesta = input("¿Te gusta programar? (sí/no): ").strip().lower()
te_gusta = respuesta == "sí"
print("¿Te gusta programar?:", te_gusta)

# MÚLTIPLES INPUTS - Usando split()
datos = input("Introduce tu ciudad y tu país, separados por coma: ")  # Ej: Sevilla,España
ciudad, pais = datos.split(",")
print("Ciudad:", ciudad.strip())
print("País:", pais.strip())

# EVAL - Interpreta expresiones matemáticas (con precaución)
expresion = input("Escribe una operación matemática (ej: 5+3*2): ")
resultado = eval(expresion)
print("Resultado:", resultado)