def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None  # Retorna None si no se encuentra el valor

def main():
    # Definimos una matriz 3x3
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Valor a buscar
    valor_a_buscar = int(input("Introduce el valor a buscar en la matriz: "))

    # Llamamos a la función de búsqueda
    resultado = buscar_en_matriz(matriz, valor_a_buscar)

    # Mostramos el resultado
    if resultado is not None:
        print(f"El valor {valor_a_buscar} se encontró en la posición: {resultado}")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")

if __name__ == "__main__":
    main()