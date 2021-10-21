# 6 - Crea un programa que pida una fecha (dia y mes, el dia debe ser numerico y el mes en string, por ejemplo: dia=23, string=Mayo) si esta fecha es tu cumpleanios entonces imprime un mesaje que lo indique, en otro caso indicar que no es tu cumpleanios. Nota: la comparacion del mes debe ser True aunque las mayusculas y minusculas no coincidan.
dia = input ("Por favor ingrese una fecha, día: ")
mes = input ("¿y el mes? ")

if int (dia) == 1 and mes.lower() == "diciembre":
    print ("Es mi cumpleaños!!")
else: 
    print ("No es mi cumpleaños :'(")
