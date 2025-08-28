# Programa 1: Búsqueda en una matriz 3x3

# Definimos la matriz 3x3
matriz = [
    [5, 2, 9],
    [1, 7, 6],
    [3, 8, 4]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra

# Valor a buscar
valor_buscar = 7

# Buscar el valor
resultado = buscar_valor(matriz, valor_buscar)

if resultado:
    print(f"El valor {valor_buscar} se encontró en la posición {resultado}")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz")


