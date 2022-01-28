import json
#Para validar los archivos json se puede usar un 'validador de json' en internet
def read_eq_data():
    filename = "C:/Users/sandr/OneDrive/Escritorio/Curso-Python/Ejercicios/Analisis_de_datos/json/Data/eq_data_30_day_m1.json"

    with open(filename) as open_file:
        eq_data = json.load(open_file)

    # Las siguientes lineas son para crear un archivo de salida
    # output_filename = "C:/Users/sandr/OneDrive/Escritorio/Curso-Python/Ejercicios/Analisis_de_datos/json/Data/output.json"
    # with open(output_filename, 'w') as output_file:
    #     json.dump(eq_data, output_file, indent=5)

    eq_dicts = eq_data["features"]
    #print(type(eq_dicts)) para validar que tipo de dato es
    mags, longs, lats = [], [], []

    #Forma 1
    # for eq in eq_dicts:
    #     properties = eq["properties"]
    #     mag = properties['mag']
    #     mags.append(mag)
    #print(mags)
    #Forma 2:
    for eq in eq_dicts:
        mag = eq["properties"]["mag"]  #Concatenamos para no escribir otra variable y extraer de cada clave el valor, se puede hacer en una linea y si hubiera mas submenues igual se agrega el dato buscado
        lon = eq["geometry"]["coordinates"][0]
        lat = eq["geometry"]["coordinates"][1]

        mags.append(mag)
        longs.append(lon)
        lats.append(lat)
    #print(mags)
    # print(longs)
    # print(lats)
    return (mags, longs, lats)


