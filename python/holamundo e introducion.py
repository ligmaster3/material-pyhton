#Inicuiamos mi propio curso e comandos de guia
print("Hola mundo")

#*****************operraciones aritemeticas**************
suma = 3 + 5
resta = 2 - 5
multi = 12 * 5
divi = 12 / 5
#si es en variable como la primera debe reflejar con print(suma)
#se pueden usar de ambas formas para representar una operacion 
#use print("25+5") con us respectiva dato para que es usuario sepa que numero es
print(25+5)
print(25-5)
print(25*5)
print(25/4)
#en el segundo caso se hace directo y ya te muestra el resultado

#potenciacion o exponente  
expo = 12 ** 5
print(expo)
print(5 ** 3)

#division baja
division_baja = 12 // 5
print(division_baja)
print(25 // 4)

#resto o modulo
resto = 12 % 5
print(resto)
print(25%4)

#"***************tipos de datos**************"

print("--datos string-caracteres-")
print("Dime tu nombre:")
nom = input()
print(nom)  
#hay otra forma de perdir al ususario datos a ingresar
nombre = input("Dime tu nombre:")
print("Hola, ", nombre)
#concatenar con + para añadir mas a la palabra
print ("Hola " + nombre + " como estas")

nombre1 = "Enier" #declaramos directamente a la varibales
print(nombre1) #motrar

#definir varibales numericas
print("--Tipo de dato con numeros--")
numer = 3
print(numer)
#aqui ay que tener cuidado ya que los datos no an sido declarados

n1= int(input("dime un numero: "))
n2 = float(input("Dime otro número: "))
print(n1)
print("el numero2 es: ", n2) 
print("la suma de ambos numeros es:",n1+n2)  #es el mismo caso que en operacion matematicas

#************Codicionales************
edad = 19
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
#----------Ejemplo 2-----------
    dato = int(input("Dime un número: "))
if dato > 0 :
    print("Es positivo")
    print("...")
else :
    print("Es negativo")
    print("o cero")
#siempre ay que tener cuidad a la hora de estructurar
#*********CICLOS ANIADOS********
nota = 85
if nota >= 90:
     print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
else:
    print("Necesitas mejorar")
#---------Ejemplo 2--------
    dia = int(input("Dime el dia de la semana: "))
if dia == 1:
    print("Lunes")
else:
    if dia == 2:
        print("Martes")
    else:
        if dia == 3:
            print("Miercoles")
        else:
            if dia == 4:
                print("Jueves")
    
#if dato != 0:
    #if dato > 0  or  dato == 0:
     #   if dato > 0  and  dato == 0:
      #      if not ( dato > 0 ) :
#************DO-WHILE*************  
respuesta = ""

while True:
   respuesta = input("Introduce 'salir' para terminar: ")
   if respuesta == "salir":
     break
        
#************REPETIR**************
for numero in range(1,6):  #1 , 2 ,3 ,4 ,5 
    print(numero)
                
veces = 5
for i in range(veces):
    print("Repetición:", i+1)
    
    #Cabe aclarar que esto es un arreglo/vector de esta forma tmb se puede crear una tupla
animales = ["perro","gato","loro","leon"]    
for animales in animales:
    print(animales) 
    #La impresion se mostraria e forma de tabla   
#**************WHILE****************
#mientras que la condicion se cumpla el ciclo se va a ejecutar
contador = 0
while contador < 10:
    print(contador)
    contador += 1 #El contador que va a ir sumandose
   
#****************************    
