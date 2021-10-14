import math

numeros = range(0, 1001) 
for value in numeros:
    if value in range(1, 1001):
        temp = (value + 1) / (value)
        print (temp)    
