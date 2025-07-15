# AND
resultado = True & True    # Devuelve True
resultado2 = False & True  # Devuelve False
resultado3 = True & False  # Devuelve False
resultado4 = False & False # Devuelve False

print("AND")
print(resultado)   # True
print(resultado2)  # False
print(resultado3)  # False
print(resultado4)  # False

# OR
resultado = True | True    # Devuelve True
resultado2 = False | True  # Devuelve True
resultado3 = True | False  # Devuelve True
resultado4 = False | False # Devuelve False

print("OR")
print(resultado)   # True
print(resultado2)  # True
print(resultado3)  # True
print(resultado4)  # False

# NOT
resultado_not1 = not True       # Devuelve False
resultado_not2 = not False      # Devuelve True

print("NOT")
print(resultado_not1)  # False
print(resultado_not2)  # True
