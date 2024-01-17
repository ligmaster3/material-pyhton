def mostrar_patron(num_filas):
    for i in range(num_filas):
        for num_columnas in range(num_filas-i):
            print("*", end="")
        print()