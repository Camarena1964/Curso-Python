def counting_letters (x):
        """Función que cuenta las veces que aparece un caracter en un texto"""
        ocurrences = {}
        for character in x:
            counter = ocurrences.setdefault(character, 0)
            ocurrences[character] = counter + 1 
        return ocurrences

paragraph = input("Por favor ingresa un texto ")
ocurrences = counting_letters(paragraph)
for key, value in ocurrences.items():
            print(f"El caracter '{key}' aparece '{value}' veces")

counting_letters("hola")

