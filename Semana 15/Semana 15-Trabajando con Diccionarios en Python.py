# 1. Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "leandro Paucar",
    "edad": 24,
    "ciudad": "Quito",
    "profesion": "Diseñador"
}

# 2. Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Quito"

# 3. Agregar una nueva clave-valor (actualizamos o agregamos profesión)
informacion_personal["profesion"] = "Diseñador Grafico"

# 4. Verificar si existe la clave "telefono", si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"

# 5. Eliminar la clave "edad"
del informacion_personal["edad"]

# 6. Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)
