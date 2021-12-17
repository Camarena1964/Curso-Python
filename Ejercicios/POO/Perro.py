def dame_un_juego_al_azar():
    return "ir por la pelota"

class Perro:
    """Una clase basica que representa a un perro"""

    def __init__(self, nombre, edad, raza):
        """inicializando el nombre y la edad del perro"""
        self.nombre = nombre
        self.edad = edad
        self.color = None
        self.raza = raza
        self.orejas = None
        self.numero_de_juegos_restantes = 3
    
    def ladrar(self):
        print(f"Hola soy {self.nombre} y digo guaaauuu")

    def jugar(self):
        if self.numero_de_juegos_restantes > 0:
            juego = dame_un_juego_al_azar()
            print(f"Hola soy un perro de la raza {self.raza} y por tanto cuando juego me divierto y ahora estoy jugando {juego}")
            self.numero_de_juegos_restantes = self.numero_de_juegos_restantes - 1
            #self.numero_de_juegos_restantes -= 1  forma corta para expresar la linea anterior
        else:
            print(f"{self.nombre} tu ya no puedes jugar amigo")
    def saludar_a_otro_perro(self, otro_perro):
        print(f"Hola soy{self.nombre} y estoy saludando a mi amigo {otro_perro.nombre}")

    def dame_nombre(self):   #Getters
        return self.nombre
    
    def escribe_nombre(self, nombre):  #Setters
        if nombre != None:
            self.nombre = nombre


#Crear una instancia
mi_primer_perro = Perro("Perri", 2, "Schnauzer")

#print(mi_primer_perro.nombre)
mi_primer_perro.ladrar()    #Usamos la funcion que definimos

#mi_primer_perro.nombre = "Firulais"  #Esto no deberia de hacerlo puede provocar errores

for i in range (5):
    mi_primer_perro.jugar()

mi_primer_perro.jugar()
mi_segundo_perro = Perro("Polo", 3, "Golden")
print(mi_segundo_perro.numero_de_juegos_restantes)

mi_primer_perro.saludar_a_otro_perro(mi_segundo_perro)