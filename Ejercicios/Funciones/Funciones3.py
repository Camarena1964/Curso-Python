# 1. Declarando parámetros por default.

def add(x=10, y=8):   #Aqui no le das espacio porque son parámetros
    return f"Suma: {x + y}"

print(add(20, 20))

def get_age(age=18):
    pass

# 2. Declarando parámetros por default y uno requerido:
"""3.Precedencia de parámetros: los parámetros sin valor por default son "parámetros requeridos" y tienen precedencia sobre los por defecto"""
def multiply(x, y, z=30):
    return f"El producto es: {x * y + z}"

print(multiply(10, 20))


def get_user_fullname(firstname, lastname, age=18, location="", blood_type=""):  #Como se definió age, se tiene que definier location y blood_type también
    pass

#4. Evitar predefinir variables y usarlas como parámetros, una vez definido un 
# por defecto el valor se conserva

CURRENT_YEAR = 2021      #Por convención en mayúscula cuando son variables globales

def calc_year_born(x, y=CURRENT_YEAR):   #Se recomienda poner directamente el valor por defecto en lugar de la variable...
    year_born = y - x 
    return f"Usted nació en el año: {year_born} :OMG!"

print(calc_year_born(30))
print(calc_year_born(30, 2025))

#5. Funciones como variables
def add2(x, y):
    print (x + y)
result = add2(8, 8)
print(result)   ##OJO print return: NONE, por eso la importancia de poner en el return un valor así:


def add2(x, y):
    return x + y
result = add2(8, 8)
print(result)
# print(add2(8, 5))

"""List Comprehensions"""
def double(x):
    return x * 2
sequence = [1, 3, 5, 9]
# mi_list = []
# for numero in sequence:      #Se pudo haber utilizado con un for pero el código es más extenso 
#     doble = double (numero)

doubled = [double(x) for x in sequence]  #or        se me atrofió el internet, minuto 11 después de la hora

print(doubled)


my_list2 = [num for num in range (0, 100)]
my_list3 = [num * 2 for num in range (0, 100)]
my_list_even4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print (my_list2)
print (my_list3)
print (my_list_even4)


#Sets de listas, no permite repetibles!
my_ls2 = [1, 2, 2, 3, 4]
my_set = set(my_ls2)
print(my_set)