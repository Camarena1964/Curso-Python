def genera_lista():
    participantes = ['Juan', 'Luis', 'Maria']
    print (participantes)
    return participantes

def genera_diccionario():
    diccionario = {'nombre' : 'Juan', 'apellido' : 'Maria'}
    return diccionario

part = genera_lista()
part[0] = "Mario"
print (genera_lista())

part = genera_lista

part()   #Esta asignandosele a la variable part una funcion por eso funciona

def execute_generator(x: function):
    return x()

print(execute_generator(genera_lista))
print(execute_generator(genera_diccionario))


