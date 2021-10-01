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