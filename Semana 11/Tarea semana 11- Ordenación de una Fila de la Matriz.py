# Programa: Ordenación completa de la matriz 3x3

# Definimos la matriz 3x3
matriz = [
    [5, 2, 9],
    [1, 7, 6],
    [3, 8, 4]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Convertir la matriz en una sola lista
lista = []
for fila in matriz:
    lista.extend(fila)

# Ordenar la lista
lista.sort()

# Reconstruir la matriz ordenada
n = len(matriz[0])  # número de columnas
matriz_ordenada = []
for i in range(0, len(lista), n):
    matriz_ordenada.append(lista[i:i+n])

# Mostrar la matriz completamente ordenada
print("\nMatriz completamente ordenada:")
for fila in matriz_ordenada:
    print(fila)


