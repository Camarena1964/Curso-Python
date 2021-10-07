#  Almacena los nombres de algunos de tus amigos en una lista llamada "nombres", despues imprime cada nombre accediendo cada elemento de la lista, uno a la vez.
nombres = ["Paco", "Alicia", "Cachet", "Dany", "Sarah"]
i = 0
while i < len(nombres): 
    print(nombres[i])
    i+=1
    
# Iniciando con la lista creada en el ejercicio anterior, en lugar de solo imprimir su nombre, imprime un mensaje para ellos, el mensaje debe ser el mismo para todos, pero personalizado con el nombre de cada amigo.
for amigo in nombres:
    print(f"Hola amigo {amigo}, nunca cambies")
