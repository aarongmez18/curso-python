
# ==============================
# MÉTODOS DE LISTAS EN PYTHON
# ==============================

# Creamos una lista de ejemplo
mi_lista = [1, 2, 3, 4]

# APPEND - Agrega un elemento al final
mi_lista.append(5)  # [1, 2, 3, 4, 5]

# EXTEND - Agrega todos los elementos de otra lista al final
mi_lista.extend([6, 7])  # [1, 2, 3, 4, 5, 6, 7]

# INSERT - Inserta un valor en una posición específica
mi_lista.insert(0, 100)  # [100, 1, 2, 3, 4, 5, 6, 7]

# REMOVE - Elimina la primera aparición de un valor
mi_lista.remove(3)  # Elimina el valor 3

# POP - Elimina y devuelve un valor de una posición (por defecto, el último)
ultimo = mi_lista.pop()       # Elimina el último elemento (7)
especifico = mi_lista.pop(1)  # Elimina el elemento en la posición 1

# CLEAR - Elimina todos los elementos de la lista
mi_lista.clear()  # []

# Reiniciamos la lista para seguir probando
mi_lista = [10, 20, 30, 40, 20, 10]

# INDEX - Devuelve el índice de la primera aparición de un valor
indice = mi_lista.index(30)  # Devuelve 2

# COUNT - Cuenta cuántas veces aparece un valor
veces = mi_lista.count(10)  # Devuelve 2

# SORT - Ordena la lista de menor a mayor
mi_lista.sort()  # [10, 10, 20, 20, 30, 40]

# REVERSE - Invierte el orden actual de la lista
mi_lista.reverse()  # [40, 30, 20, 20, 10, 10]

# COPY - Crea una copia de la lista
copia_lista = mi_lista.copy()  # copia_lista = [40, 30, 20, 20, 10, 10]

# LEN - Devuelve la longitud de la lista (no es método, es función)
longitud = len(mi_lista)  # 6

# Mostramos algunos resultados
print("Lista final:", mi_lista)
print("Índice de 30:", indice)
print("Cantidad de 10:", veces)
print("Copia de la lista:", copia_lista)
print("Longitud de la lista:", longitud)
