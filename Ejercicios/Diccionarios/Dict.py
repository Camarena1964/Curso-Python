dict = {
    "Ambulancia":"Krankenwagen",
    "Árbol":"Baum",
    "Flores":"Blumen",
    "Bicicleta":"Fahrrad",
    "Animal":"Tier",
    "Fruta":"Früchte"
}

query = input("Por favor ingresa la palabra que quieras consultar: ")
if query in dict:
    print(f"La traducción de '{query}' en alemán es: '{dict[query]}'")
else:
    print ("Esa palabra no está en el diccionario aún, intenta otra ")

    # query = input("Por favor ingresa la palabra que quieras consultar ")
# for query,value in dict.items():
#     if query in dict.items():
#         print(value)
#         break
# else:
#     print ("Esa palabra no está en el diccionario aún, intenta otra ")