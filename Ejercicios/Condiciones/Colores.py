# 7.1 - Crea una lista con 10 colores, crea una segunda lista con tus colores favoritos.
# 7.2 - Imprimer un mensaje si alguno de tus colores favoritos esta dentro de la lista de colores.

colores = ["Gris", "Rojo", "Verde", "Amarillo", "Negro", "Café", "Blanco", "Azul", "Rosa", "Naranja"]
favoritos = ["Azul", "Negro", "Naranja"]

# for color in favoritos:
#     for color2 in colores:
#         if color == color2:
#             print (f"{color}, este es de mis colores favoritos!") 

for color in favoritos:
    if color in colores:
        print (f"{color}, este es de mis colores favoritos!")
