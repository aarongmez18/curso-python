# ==================================
# MÉTODOS DE DICCIONARIOS (JSON) EN PYTHON
# ==================================

# Creamos un diccionario de ejemplo

persona = {
    "nombre": "Aarón",
    "edad": 30,
    "ciudad": "Sevilla"
}

# GET - Devuelve el valor de una clave, evita error si no existe
nombre = persona.get("nombre")  # "Aarón"
pais = persona.get("pais", "No especificado")  # "No especificado"

# KEYS - Devuelve todas las claves
claves = persona.keys()  # dict_keys(['nombre', 'edad', 'ciudad'])

# VALUES - Devuelve todos los valores
valores = persona.values()  # dict_values(['Aarón', 30, 'Sevilla'])

# ITEMS - Devuelve pares (clave, valor)
items = persona.items()  # dict_items([('nombre', 'Aarón'), ('edad', 30), ('ciudad', 'Sevilla')])

# UPDATE - Actualiza valores o añade nuevas claves
persona.update({"edad": 31, "pais": "España"})

# POP - Elimina una clave y devuelve su valor
ciudad = persona.pop("ciudad")  # "Sevilla"

# POPITEM - Elimina el último par clave-valor
ultimo = persona.popitem()  # ('pais', 'España')

# SETDEFAULT - Devuelve valor si existe, si no lo crea con valor por defecto
telefono = persona.setdefault("telefono", "No disponible")  # "No disponible"

# COPY - Crea una copia del diccionario
copia_persona = persona.copy()

# CLEAR - Elimina todos los elementos del diccionario
persona.clear()

# Mostramos resultados
print("Nombre:", nombre)
print("País:", pais)
print("Claves:", list(claves))
print("Valores:", list(valores))
print("Items:", list(items))
print("Edad actualizada:", copia_persona.get("edad"))
print("Ciudad eliminada:", ciudad)
print("Último eliminado:", ultimo)
print("Teléfono:", telefono)
print("Copia del diccionario:", copia_persona)
print("Diccionario original después de clear():", persona)