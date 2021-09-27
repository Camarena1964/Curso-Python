#Crea un programa que pida la base y la altura de un triangulo y calcule el área.
base=input("¿Cuál es la base de tu triángulo? ")
altura=input("¿Cuál es la altura de tu tiángulo? ")
base=float(base)
altura=float(altura)
area=((base*altura)/2)
print(f"El área de tu triángulo de base {base} y altura {altura} es: {area}")