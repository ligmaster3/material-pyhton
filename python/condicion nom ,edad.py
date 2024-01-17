nombre = input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")
print("Hola, ", nombre+" "+apellido)
edad = int(input("Dime tu edad: "))
if edad >= 18:
    print("Eres mayor de edad."+nombre)
else:
    print("Eres menor de edad."+nombre)
