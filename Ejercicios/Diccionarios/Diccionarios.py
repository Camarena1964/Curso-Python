"""Caracteristicas:
1. Los diccionarios se usan para guardar valores de datos en pares clave:valor
2. Desde Python 3.7 son ordenados (los indices fijados en memoria)
3. Son mutables y no permite duplicados"""
 
my_dic = {}
print (my_dic)

products = {
    "fruits": ["mango", "banana"],
    "veggies": ["apio", "papa"],
    "nuts": ["peanuts"]
}

# Crear un diccionario con claves duplicadas
print("1. Diccionario duplicado")
dict_duplicado = {
    "2":2,
    "2":5
}
print(dict_duplicado)  # Sólo imprime el segundo valor porque no se duplican los valores se imprime la reasignación
print(f"{'*'*20}\n")

#Crear un diccionario variado
print("2, Diccionario variado")
varied_dict={
    "integer": 1,
    "string": "hola",
    "boolean": True,
    "float": 35.99,
    "list": [1, 2.5, "tres", False],
    "tuple": ("hello",),
    "another_dict":{"month":"Enero", "year":2021},
    "set": {"apple", "banana", "cherry"}
}
print(varied_dict)
print(f"{'*'*20}\n")

#Vaciar un diccionario
print("3, Diccionario vacío")
empty_dict={
    "product":"compu"
}
empty_dict.clear()
print(empty_dict)
print(f"{'*'*20}\n")

#Copiar un diccionario
dict1 = {
    "2":"dos",
    "3":"tres",
    "4":"cuatro"
}
print("4, Diccionario copiado")
dict2 = dict1.copy()
print("Copiado")
print(dict2)
print(f"{'*'*20}\n")

#Acceder a un valor por su clave
print("5. Acceder a un valor por su clave")
print(dict1["2"])  # Ejemplo 1
value2 = dict1["2"]  # Para extraer un valor del diccionario y guardarlo en una variable

print(dict1.get("9", "nada aquí"))  # Ejemplo 2

print(f"{'*'*20}\n")

#Mostrar valores
print("6. Imprimir solo valores")
dict_keys = dict1.keys()
dict_values = dict1.values()  # Estamos creando nuevamente una nueva variable para guardar los valores
print(dict_values)
print(dict_keys)
print(f"{'*'*20}\n")

#Imprimir clave y valor
print("7. Imprimir clave y valor")
for key, value in dict1.items():
    print(key, value)
    print(dict1.items())
print(f"{'*'*20}\n")

#Ejercicio: Checar si existen una clave y un valor específicos en el diccionario
print("8. Checando si están la clave:valor específicos")

#Insertar clave y valor si no existen
print("9. Insertar clave y valor si no existe")
dict1.update({"5": "cinco"})
print(dict1)
print(f"{'*'*20}\n")

#Editar valor
print("10. Editar valor")
dict1.update({"2": "doss"})
print(dict1)

print(f"{'*'*20}\n")

#Insertar clave y valor si no existe, si existe lo retorna, no lo edita
print("11. Insertar clave y valor si no existe, si existe lo retorna, no lo edita")
dict1.setdefault("7", "siete")
dict1.setdefault("7", "SIETE")
print(dict1)
print(f"{'*'*20}\n")

#Insertar clave y valor si no existe, si existe lo retorna, no lo edita
print("12. Insertar clave y valor si no existe, si existe lo retorna, no lo edita")
dict1 = {**dict1, **{"6": "seis"}}  #Destructurizando, hay que investigar más porque es avanzado
print(dict1)
print(f"{'*'*20}\n")

#Editar clave
print("13. Editar clave")
dict1["2s"] = dict1.pop("2")  #Editamos la clave usando el método pop, quita un valor y asigna nuevamente
print(dict1)
print(f"{'*'*20}\n")

#Retornando un diccionario agregando con claves y valores declarados
print("14. Retornando un diccionario de los valores declarados")
x = ["Key1", "Key2"]
c = ""
dict3 = dict.fromkeys(x, c)
print (dict3)
