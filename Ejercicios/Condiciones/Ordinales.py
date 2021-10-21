# 2 - Crea una lista con los numeros (tipo entero) del 1 al 9. Itera la lista y crea una cadena de if-elif-else dentro del ciclo, para imprimir el numero ordinal, por ejemplo para el 1 -> primero, 2 -> segundo, etc. Cada numero se debe imprimir en una linea diferente.

numeros = list(range(1,10))
for numero in numeros:
    if numero == 1:
        print ("Primero")
    elif numero == 2:
        print ("Segundo")
    elif numero == 3:
        print ("Tercero")
    elif numero == 4:
        print ("Cuarto")
    elif numero == 5:
        print ("Quinto")
    elif numero == 6:
        print ("Sexto")
    elif numero == 7:
        print ("Septimo")
    elif numero == 8:
        print ("Octavo")
    elif numero == 9:
        print ("Noveno")