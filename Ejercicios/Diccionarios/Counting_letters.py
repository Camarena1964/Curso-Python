"""Programa que recibe como input un párrafo de texto y al final  va a mostrarnos cuántas veces aparece cada letra en ese texto"""

paragraph = "Un polímero (del griego: πολυς [polys]mucho y μερος [meros] parte o segmento     ) es una sustancia compuesta por grandes moléculas, o macromoléculas (generalmente orgánicas) formadas por la unión mediante enlaces covalentes de una o más unidades simples llamadas monómeros.3​ Debido a su gran variedad de propiedades, tanto los polímeros sintéticos como los naturales juegan un rol esencial en nuestras vidas.4​ Los polímeros abarcan tanto a los plásticos sintéticos que todos conocemos, como el polietileno, así como los biopolímeros naturales como el ADN y las proteínas, que son fundamentales para la estructura y funcionamiento biológico.El polisopreno (del hule o caucho), es un ejemplo de un polímero natural, y el poliestireno (de la espuma o empaques de poliestireno) es un ejemplo de un polímero sintético. En un contexto biológico, esencialmente todas las macromoléculas, por ejemplo: las proteínas (poliamidas), ácidos nucleicos (polinucleótidos) y polisacáridos, están compuestas en gran parte por polímeros.Los polímeros naturales y sintéticos son creados a partir de la polimerización de varios monómeros. Su gran masa molecular en comparación con otras moléculas de menor talla le aporta (a los polímeros) propiedades físicas únicas que incluyen dureza, alta elasticidad, visco elasticidad y una tendencia a formar estructuras amorfas y/o semi-cristalinas en lugar de cristales.El término de “polímero” fue propuesto en 1833 por Jöns Jacob Berzelius, con una definición distinta a la definición moderna de la IUPAC.5​ El concepto actual de polímeros como estructuras macromoleculares unidas de manera covalente fue propuesto en 1920 por Herman Staudinger;6​ quien dedicó una década a buscar pruebas experimentales para sustentar esta hipótesis.7​Los polímeros son estudiados en los campos de ciencia de polímeros (que incluye la química de polímeros y física de polímeros), la biofísica y la ciencia de materiales e ingeniería. Históricamente, los productos que resultan de la unión de unidades repetitivas por medio de enlaces covalentes han sido el enfoque principal de la ciencia de polímeros. Sin embargo, actualmente un área emergente de investigación se centra en polímeros supramoleculares que se forman a través de enlaces no covalentes"
ocurrences = {}
for character in ocurrences:
    if character in paragraph:
        ocurrences[character] += 1
    else:
        ocurrences.update({character : 1})
print (ocurrences)

# for k in ocurrences:
#     print(f"El caracter '{k}' aparece {ocurrences[k]} veces")

#dic.items() -> retorna una lista de tuplas
#[('T', 1), ('w', 4)...]

#Opción 2
for key, value in ocurrences.items():
    print(f"El caracter {key} aparece {value} veces")

#Opción 3
for im_a_tuple in ocurrences.items():
    print(f"El caracter '{im_a_tuple[0]}' aparece {im_a_tuple[1]} veces")

#Destructuring tuples
t = (1,2,3)
x,y,z = t

#Opción 3
ocurrences = {}
print(ocurrences.get("a",0))

#1 - La key si existe -> Retorna el valor actual
#2 - La key no existe -> Inserta un nuevo elemento 
for character in paragraph:
    counter = ocurrences.setdefault(character, 1)
    ocurrences[character] = counter + 1
    counter += 1

for key, value in ocurrences.items():
    print(f"El caracter {key} aparece {value} veces")