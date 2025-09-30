# Autor: Estefanía Narváez
# Tarea: Trabajo con Archivos de Texto en Python
# Fecha: Septiembre 2025

# -------------------------------
# 1. Escritura de Archivo de Texto
# -------------------------------
# Abrimos el archivo en modo escritura ("w") y agregamos notas
file = open("my_notes.txt", "w")  # crea el archivo o lo sobrescribe

file.write("Primera nota: Estoy aprendiendo archivos en Python.\n")
file.write("Segunda nota: Usando write() y readline().\n")
file.write("Tercera nota: Este archivo es parte de la tarea.\n")

file.close()  # cerramos el archivo después de escribir

# -------------------------------
# 2. Lectura de Archivo de Texto
# -------------------------------
file = open("my_notes.txt", "r")  # abrimos en modo lectura

# leemos línea por línea con readline()
linea1 = file.readline()
print(linea1.strip())

linea2 = file.readline()
print(linea2.strip())

linea3 = file.readline()
print(linea3.strip())

file.close()  # cerramos el archivo después de leer

