#Pedir al usuario un número del 1 al 1024 e imprimir este número en binario
valor=input("Por favor ingrese un número del 1 al 1024 que desee conocer su codificación en binario ")
valor=int(valor)
binario=bin(valor)
if valor >1024:
    print("Te dije que hasta 1024!!!  Intenta nuevamente, por favor ingresa un nuevo número del 1 al 1024")
else:
    print(f"La codificación en binario de '{valor}' es '{binario}")
