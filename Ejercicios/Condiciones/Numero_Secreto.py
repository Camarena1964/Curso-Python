import random
random.seed()
numeros = random.randint(1,100)
numero_usuario = 0
while numero_usuario != numeros:
    print ("Intenta adivinar el numero secreto, ingresa un numero entre el 1 y el 100")
    numero_usuario = int (input("Cual es tu numero \n"))
    if numeros != numero_usuario:
        print ("El numero que tu ingresaste no es el numero secreto")
    else:
        print ("Ese es el numero secreto, felicidades")
    


