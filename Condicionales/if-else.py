# Primer bloque
iguales = "Son Iguales"
no_iguales = "No son iguales"

if 1 == 2:
    print(iguales)  # Esto NO se ejecuta
else:
    print(no_iguales)  # Esto SÍ se ejecuta

print("No forma parte de ninguna condición")

# Segundo bloque
if 3 == 2:
    print(iguales)  # Esto NO se ejecuta
elif 2 == 2:
    print(iguales)  # Esto SÍ se ejecuta
else:
    print(no_iguales)
