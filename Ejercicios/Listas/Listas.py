import sys
#Acceder a los valores de la lista/tuple
lista=[1, "hola", 20.5, False, False]
mi_tuple=()

print(type(lista))
print(type(mi_tuple))

"""Saber el tamaño de una lista o un tuple"""
print(f"Tamaño en memoria de la lista: {sys.getsizeof(lista)}")
print(f"Tamaño en memoria del tuple: {sys.getsizeof(mi_tuple)}")

"""Acceder a los valores de una lista o un tuple por medio de su valor del índice."""
lista2 = [1, 2, "Panchito", 4, 5]
tuple2 = (6, 7, 8, 8, "hola")  #El indice en python inicia de 0 1 2 3...

print(lista2[2])
print(tuple2[4])

#Acceder al último valor de una lista o tuple
print(lista2[-1])
print(tuple2[-1])

#len () es para saber qué tantos valores hay dentro de un objeto
print(len(lista2))
print(len(tuple2))

#Editar valores de una lista 
lista3 = [9, 8, 7, 6, 5]
tuple3 = (7, 7, 6, 1)

lista3[0] = "love"
#tuple[-1] = 9    #No se puede!!!

print(lista3)

lista3.insert(1, "niña")
print(lista3)

lista3.append("el último")
print(lista3)

nombre = "Panchito"
#print(nombre.)  #Control+espacio para ver lo que puedes hacer con el tipo de objeto

"""Lista con algunos presidentes de México"""

presidentes = ["Andres Manuel", "Enrique Peña", "Felipe Calderón", "Vicente Fox"]
print (presidentes)

for presidente in presidentes:
    print(f"Hola {presidente}, cuánto dinero te robaste?")
    print("Devuelve el dinero, no seas ratero")

for valor in range(1, 1000):
    print (valor)

for indice in range (0, len(presidentes)): #el cero pudo haberse omitido, porque si no lo pones el inicio en automático es cero
    print (presidentes[indice])

for valor in range (0, 20, 2): #el incremento es de 2 en 2
    print (valor)

for valor in range(20):
    print (valor)


digitos = list(range(10))
print (digitos)
print (max(digitos))
print (min(digitos))
print (sum(digitos))
print (sum(digitos) / len(digitos))

"""Código para generar la lista de cuadrados de un rango versión 1"""

cuadrados = []
for value in range (1, 11):
    cuadrado = value **2
    cuadrados.append(cuadrado)
print (cuadrados)

"""Código para generar la lista de cuadrados de un rango versión 2"""
cuadrados = [value **2 for value in range (1, 11)]  #si le pones str antes de value: str (value) te regresa valores de cadena
print (cuadrados)

"""Vaciar una lista"""
invitados = ["Luis", "José", "Adrián", "Fernando", "Juan"]
while len(invitados) > 2:
    invitado = invitados.pop()
    print(f"{invitado}, tu ya no estás invitado")

print (invitados)

# ultimos_presidentes = presidentes [:2] # Desde el principio hasta el valor dos
# ultimos_presidentes = presidentes [2:] # Desde el segundo valor hasta el final de la lista
# ultimos_presidentes = presidentes [-1:] #último valor hasta el último
# ultimos_presidentes = presidentes [-2:] #Desde el penúltimo valor hasta el último
# ultimos_presidentes = presidentes [0:2]
# print (ultimos_presidentes)
for presidente in presidentes[1:]:
    print(f"{presidente} Tu ya no eres presidente")


