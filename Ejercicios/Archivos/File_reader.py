filename = "Ejercicios\\Archivos\\pi_digits.txt"
executed = True

try:
    with open ('Ejercicios\\Archivos\\pi_digits.txt') as file_object:
        lines = file_object.readlines()
    #with open ('C:\\Users\\sandr\\Desktop\\Curso-Python\\Archivos\\pi_digits.txt') as file_object:
        # for line in file_object:
        # #content = file_object.read()
        #     print(line.rstrip())

    pi_string = ""
    for line in lines:
        pi_string = pi_string + line.strip()

    birthday = input("Ingresa tu fecha de cumpleanios en el formato ddmmaa: ")

    if birthday in pi_string:
        print(f"Tu fecha de cumpleanios {birthday}, se encuentra en el millon de digitos de pi")
    else:
        print(f"Tu fecha de cumpleanios {birthday}, no se encuentra en el millon de digitos de pi")
except FileNotFoundError:
    print("El archivo que intentaste abrir no existe")