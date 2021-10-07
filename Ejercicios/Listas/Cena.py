# 4.1 - Si pudieras invitar a cualquiera a cenar (vivo o muerto) a quien invitarias? Crea una lista con al menos 3 personas, despues usa esta lista para imprimir un mensaje para cada uno de ellos invitandolos.
# 4.2 - Entonces escuchaste que uno de tus invitados no podra asistir a tu cena, necesitas enviar una nueva invitacion a alguien mas. Utilizando como base el punto anterior, comienza agregando un print del invitado que no podra asistir, reemplaza el invitado que no podra asistir con el nombre del nuevo invitado (utilizando alguno de los metodos de las listas). Al final imprime un mensaje de invitacion para los nuevos invitados.
# 4.3 - Imagina que has encontrado una mesa mas grande y por tanto puedes invitar mas amigos a tu cena. Utilizando como base el punto anterior, comienza agragando un mensaje al final que diga que has encontrado una mesa mas grande y vas a invitar a mas amigos. Agrega 3 nuevos invitados a tu cena, agrega a uno de ellos al inicio, otro a la mitad y al tercero al final de la lista. Al final muestra los mensajes de invitacion para todos los invitados.
# 4.4 - Cuando llega el dia de la cena te dicen que desafortunadamente la mesa que te habia reservado no estara disponible, entonces solo pueden ofrecer una mesa para 3 y por esto solo puedes mantener a 2 invitados. Utilizando como base el punto anterior, comienza agregando un mensaje al final que diga que desafortunadamente solo podras tener 2 invitados en tu cena. Elimina a tus invitados uno a uno hasta que te quedes con unicamente 2, Cada que elimines uno de ellos de la lista imprime un mensaje de disculpa por no poder invitarlo a la cena. Despues imprime un mensaje para cada uno de los invitados que quedaron en la lista que diga que ellos siguen invitados. Al final del programa imprime un mensaje que diga como les ha parecido la cena.
invitados = ["Paco", "Fati", "Mamá", "Papá", "Vero"]
for nombre in invitados:
    print (f"Hola {nombre}, me gustaría que me acompañaras a cenar el próximo sábado, ¿puedes y quieres?")

print (f"Hola, desafortunadamente {invitados[4]} no podrá acompañarnos a cenar por lo que tendremos que invitar a alguien más")
invitados[4] = "Jesús"
print (f"Hola {invitados[4]}, me gustaría que me acompañaras a cenar el próximo sábado, ¿puedes y quieres?")

print ("Hola a todos, he encontrado una mesa más grande, invitaré a más personas a que cenen con nosotros")
invitados.insert(0, "San Francisco")
invitados.insert(2, "Padre Pío")
invitados.append("Virgencita")

for nombre in invitados:
    print (f"Hola {nombre}, me gustaría que me acompañaras a cenar el próximo sábado")

print(f"Los invitados a la cena del sábado son: {invitados}")

print ("Hola a todos! los HSPM me cancelaron una mesa por lo que sólo puedo invitar a dos de ustedes esta ocasión")

# i = 0
# while i <len(invitados):
#     if (i<=5):
#         print (f"{invitados[i]}, lo siento, esta vez no podremos cenar juntos, prometo organizar una nueva cena pronto para ir juntos")
#     if (i>5):
#         print (f"{invitados[i]}, tu sigues invitado a la cena")
#     i+=1

print(invitados)

print(f"Lo siento amigo {invitados[0]} en esta ocasión no te puedo invitar a la cena")
invitados.pop(0)
print(f"Lo siento amigo {invitados[0]} en esta ocasión no te puedo invitar a la cena")
invitados.pop(0)
print(f"Lo siento amigo {invitados[0]} en esta ocasión no te puedo invitar a la cena")
invitados.pop(0)
print(f"Lo siento amiga {invitados[0]} en esta ocasión no te puedo invitar a la cena")
invitados.pop(0)
print(f"Lo siento amiga {invitados[0]} en esta ocasión no te puedo invitar a la cena")
invitados.pop(0)
print(f"Lo siento amigo {invitados[0]} en esta ocasión no te puedo invitar a la cena")
invitados.pop(0)

print(invitados)

print(f"{invitados[0]} Tu sigues invitado a la cena")
print(f"{invitados[1]} Tu sigues invitada a la cena")

print (f"{invitados[-1]}, {invitados[-2]}, ¿Qué les pareció la cena?")
    



