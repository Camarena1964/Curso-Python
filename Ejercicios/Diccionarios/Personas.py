names = ["Fatima", "Fernando", "Francisco", "Maria", "Juan", "Jorge", "Sandra", "Joel", "Carlos", "Montserrat", "Veronica"]
dict = {}
# Version 1
for name in names:
    initial = name [0]

    if dict.get(initial) == None:
        dict.update({initial: [name]})
        # lista = []
        # lista.append(name)
        # dict.update({initial: lista})
    else:
        dict.get(initial).append(name)
print(dict)

# Versión 2
dict = {}
for name in names:
    dict.setdefault(name [0], []).append(name)
print(dict)