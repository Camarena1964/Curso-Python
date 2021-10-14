import math

numeros = list(range(100))
for value in range (1 , 100, 2):
    print (value)

millon = list(range(1000001))
print (sum(millon))

raiz = [math.sqrt(value) for value in range(1, 101)]
print (raiz)

numeros2 = list(range(100, 111))
i = 0
lista2 = []
while len(numeros2) > i:
     value = numeros2[len(numeros2)-1-i]
     lista2.append(value)   
     i=i+1
print (lista2)

numeros2 = list(range(100, 111))
i = 0
while len(numeros2)/2 > i:
    temp = numeros2[len(numeros2)-1-i]
    numeros2[len(numeros2)-1-i] = numeros2[i]
    numeros2[i] = temp
    i=i+1
print(numeros2)
    

