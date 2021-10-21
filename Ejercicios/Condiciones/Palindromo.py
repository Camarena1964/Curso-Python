# 3 - Crea un programa que lea una frase desde el teclado e imprima un mensaje que indique si esa palabra es un palindromo o no (https://es.wikipedia.org/wiki/Pal%C3%ADndromo), Tip: los strings tambien son indexados como las listas, por tarto se pueden iterar exactamente igual.
frase = input("Por favor ingresa una frase o palabra \n") 

# for i in range (len(frase)):
#     if frase[len(frase)-1-i] == frase [i]:
#         salida = True
#     else:
#         salida = False
#         break
# if salida == True:       
#     print ("Esto es un palíndromo")
# else:
#     print ("Esto no es un palíndromo")

si_es = True
for i in range (len(frase)):
    if frase[len(frase)-1-i] != frase [i]:
        si_es = False
        break
if si_es == True:       
    print ("Esto es un palíndromo")
else:
    print ("Esto no es un palíndromo")
    






# salida = False
# a = len(frase)
# for i in frase:
#     while a <= len(frase):
#         s = 
#         if i == s:
#             salida = True
#             a = a-1
#         print ("Esto es un palindromo")
#     else:
#         ("Esto no esun palindromo")


    # a = len(frase)
    # for a in frase:
    #     if i == a:
    #         salida = True
    #         a = a-1
    #     print ("Esto es un palindromo")
    # else:
    #     ("Esto no esun palindromo")