i=0
dict_name={}
while i < 5:
    name = input ("¿Cuál es tu nombre? ")
    number = input ("¿Cuál es tu número favorito? ")
    dict_name.update({name : number})
    i=i+1
print (dict_name)


