"""-Un parámetro es la variable enlistada dentro del paréntesis en la definición de la función
-Un argumento es el valor que es enviado a la función cuando es invocada
-El número de parámetros en la función pide el mismo número de argumentos cuando sea invocada"""

NAMES = ["sandra", "paco"]
def saludar_a_alguien():
    """Saludar a alguien."""
    #pass        #Le agregas pass si no va a llevar cuerpo temporal para que puedas seguir trabajando...
    name = "Panchito"
    return name

saludar_a_alguien()
print(saludar_a_alguien())

def sumar_numeros():
    result = 20 + 20
    return result

def restar_numeros(x,y):
    result = x - y
    return result

print(f"Su resultado es {restar_numeros(10,5)}")    #Dimos valores en argumentos y da resultado :)
print(sumar_numeros())

def multiplicar_numeros (x,y):
    pass

def dividir_numeros (x,y):
    pass

def verb_noun(name):  #name es un parámetro, valor pasado a una función en su declaración
    pass

def hello_world(name):
    return f"hello {name.title()}"


###  11/11/2021 mas tema de funciones
"""2 positional arguments"""
def describe_animal (tipo, nombre):
    print(f"Tengo un animal del tipo{tipo}")
    print(f"Mi {tipo} se llama {nombre}")

# describe_animal("perro", "perry")
# describe_animal("perro", "firulais")

mascotas = [("Gato", "Garfield"), ("Conejo", "Bugs Bunny"), ("Perro", "Perry")]
for mascota_nombre in mascotas:
    describe_animal(mascota_nombre[0], mascota_nombre[1])   #La relación es uno a uno, si se define en la función 2 paraemetros espera 2 argumentos, entonces lo que se escribba en la primera posición es el primer parámetro 

"""2 keyword arguments"""
def describe_animal_argumentos_keyword (tipo = "Perro", nombre = "Perry"):
    print(f"Tengo un animal del tipo{tipo}")
    print(f"Mi {tipo} se llama {nombre}")

describe_animal_argumentos_keyword()

"""llamar funciones desde otras funciones"""
def x():
    print ("Estoy en la función x")
    y()

def y():
    print ("Estoy en la función y")
    z()

def z():
    print ("Estoy en la función z")

x()

def x():
    y()
    print ("Estoy en la función x")

def y():
    z()
    print ("Estoy en la función y")

def z():
    print ("Estoy en la función z")

x()

print(x())

#Invocación de funciones con valor de retorno de otras funciones
def suma(a, b):
    return a + b

def factorial(x):
    if (x == 1): return 1
    return x * (factorial(x - 1))

x, y, z = 15, 8, 3
print(suma(x, suma(x, suma(z, factorial (y)))))