class Perro:
    """Una clase basica que representa a un perro"""

    def __init__(self, nombre, edad, raza):
        """inicializando el nombre y la edad del perro"""
        self.nombre = nombre
        self.edad = edad
        self.color = None
        self.raza = raza
    
    def ladrar(self):
        print(f"Hola soy {self.nombre} y digo guaaauuu")

    def jugar(self):
        print(f"Hola soy un perro de la raza {self.raza} y por tanto cuando juego me divierto")

    def saludar_a_otro_perro(self, otro_perro):
        print(f"Hola soy{self.nombre} y estoy saludando a mi amigo {otro_perro.nombre}")


#Crear una instancia
mi_primer_perro = Perro("Perri", 2, "Schnauzer")

#print(mi_primer_perro.nombre)
mi_primer_perro.ladrar()    #Usamos la funcion que definimos
mi_segundo_perro = Perro("Polo", 3, "Golden")

mi_primer_perro.saludar_a_otro_perro(mi_segundo_perro)