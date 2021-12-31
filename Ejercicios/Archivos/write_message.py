filename = "Ejercicios\\archivos\\programming.txt"

with open(filename, "a") as file_object:  #w es para escribir, sobre escribe, #a, agrega al final, puede agregar, modo w pone el cursor al inicio, el modo a lo pone hasta el final
    file_object.write("I love programming a lot.\n")
    file_object.write("I really love it.\n")