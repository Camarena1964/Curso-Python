# 5.1 - Piensa en 5 o mas lugares del mundo que te gustaria visitar, agregalos estos lugares a una lista, asegurate que no esten en orden alfabetico. Imprime los lugares en el orden en que fueron ingresados (no necesitas imprimir uno por uno, puedes imprimir toda la lista). Imprime nuevamente la lista usando la funcion "sorted" (https://docs.python.org/es/3/library/functions.html#sorted). Imprime la lista nuevamente y asegurate que la lista original no se ha modificado (los elementos estan aun en el orden inicial).
# 5.2 - Despues imprime nuevamente los lugares ordenados en orden inverso utilizando la funcion "sorted" (Por ejemplo: "Viena", "Paris", "Nueva York" ...). La lista original debe seguir sin modificarse (imprimela nuevamente).
# 5.3 - Utiliza el metodo "reverse" para invertir el orden de tu lista e imprimela en este orden (asegurate que el contenido de la lista ha sido modificado).
# 5.4 - Nuevamente utiliza el metodo "reverse" para invertir la lista, asegurate que la lista se imprime en el orden inicial.
# 5.5 - Utiliza el metodo "sort" (nota: no la funcion "sorted") para ordenar la lista en orden alfabetico e imprime la lista, asegurate que la ha sido modificado.
# 5.6 - Nuevamente utiliza el metodo sort para ordenar la lista en orden inverso (Por ejemplo: "Viena", "Paris", "Nueva York" ...).

lugares_l = ["Canadá", "Bali", "Tierra Santa", "Dinamarca", "Medjugorje", "Grecia"]
print (lugares_l)
print (sorted(lugares_l))
print (lugares_l)
print (sorted(lugares_l, reverse = True))
print (lugares_l)
lugares_l.reverse()
print (lugares_l)
lugares_l.reverse()
print (lugares_l)
lugares_l.sort()
print (lugares_l)
lugares_l.sort(reverse=True)
print (lugares_l)


