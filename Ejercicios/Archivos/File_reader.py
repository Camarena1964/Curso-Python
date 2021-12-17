with open ('Ejercicios\\Archivos\\pi_digits.txt') as file_object:
#with open ('C:\\Users\\sandr\\Desktop\\Curso-Python\\Archivos\\pi_digits.txt') as file_object:
    for line in file_object:
    #content = file_object.read()
        print(line.rstrip())

print(content)