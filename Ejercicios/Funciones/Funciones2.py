"""Importing a function"""

from Funciones import (hello_world, restar_numeros, saludar_a_alguien)

NAMES = ["Sandra", "Paco", "Fátima"]

def my_function():
    name = NAMES [0]
    print(hello_world(name))

my_function()


from Ejercicios import (counting_letters)

counting_letters()
