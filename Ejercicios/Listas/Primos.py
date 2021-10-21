# import math
# from typing_extensions import TypeVarTuple

#Cálculo de factorial
# numeros = range(0, 1001) 
# resultado = 1
# for value in range (1, 10):
#     resultado *= value   
#     print (resultado)                        

# numeros = range(0, 1001) 
# resultado = 1
# for value in range (1, 10):
#     resultado /= value   
#     print (resultado)

numeros = range (0, 1001)
primos =[]
es_primo = True

for i in range (2, len(numeros)):
    es_primo = True
    for n in range (2, i):
        if i % n == 0:
            es_primo = False
            break
    if es_primo == True:
        primos.append(i)
print (primos)
        
# def es_primo(n):
    
