

nombre = input("Ingrese el nombre: ")
cantidad = int(input("Ingrese la cantidada: "))
precio = float(input("Ingrese el precio: "))

monto = precio * cantidad

itbm = monto * 0.07
total = monto + itbm

print("nombre del articulo",nombre)
print("monto a pagar: ",monto)
print("ITBM: ",itbm)
print("Total: ",total)
