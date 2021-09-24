#Programa que pide un valor en grados centígrados y lo muestra en grados farenheit
#0 °C × 9/5) + 32 = 32 °F

grados_celsius=input("Por favor ingresa el valor en grados celsius\n")
grados_celsius= float (grados_celsius)
grados_farenheit= ((grados_celsius * (9/5)) + 32)

print(f"El resultado en grados Farenheit de {grados_celsius} °C son {grados_farenheit} °F ")