# carros = ["audi", "bmw", "subaru", "toyota"]

# """Imprimir todos los carros con la inicial en mayúscula, excepto BMW que todas las letras son minúsculas"""
# for carro in carros:
#     if carro.lower () == "bmw": #El .lower nos ayuda a poner todas las letras en minúscula por si hubiera alguna mayúscula en las variables porque lo que estoy buscando son variables con minúsculas
#         print(carro.upper()) #.upper para que todo sea mayúscula
#         print("Es mi marca favorita")
#     else:
#         print(carro.title()) #.title: Para cambiar la primera letra, hacerla mayúscula

#     # valor = 150
#     # print (5==5) Arroja un booleano, true or false

# """Imprimir todos los carros excepto Audi"""
# for carro in carros:
#     if carro != "audi":
#          print (carro)

# """Comparaciones con números"""
# edad = 18
# print (edad == 18)

# numero_favorito = input("Ingresa mi numero favorito: ")
# if int (numero_favorito) == 15: #Se tiene que convertir a entero porque si no compara string con numero y no funciona
#     print ("Correcto, ese es mi numero favorito")
# else:
#     print ("Fallaste, ese no es")

# """Operadores booleanos"""
# edad = 25
# print(edad < 25)
# print(edad > 25)
# print(edad <= 25)
# print(edad >= 25)

# """Multiples condiciones"""
# """Operador and"""
# edad = 15
# if edad >= 12 and edad <= 18:
#     print ("Eres un adolescente")

# """Operador or"""
# if edad < 12 or edad > 18:
#     print ("No eres un adolescente")

#Busqueda de un valor en una lista version 1:
# numeros=[2,9,45,62,1,3]
# busqueda=5
# salida = False
# for numero in numeros:
#     if numero == busqueda:
#         salida = True
#         print ("Este valor si se encuentra en la lista")
# if salida == False:
#         print ("Ese valor no se encuentra en la lista")   

# Busqueda de un valor en una lista version 2:
numeros=[2,9,45,62,1,3]
busqueda=4
if busqueda in numeros:
    print ("Si se encuentra")
else:
    print ("No se encuentra")

"""Calcular el costo del ticket en selva magica"""
edad = 45
costo = 0
if edad < 4:
    costo = 0
elif edad < 18:
    costo = 80
else:
    costo = 150
print(f"Debes pagar {costo} pesos")