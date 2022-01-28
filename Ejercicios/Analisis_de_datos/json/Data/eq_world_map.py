from eq_explore_data import read_eq_data
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


mags, longs, lats = read_eq_data()

#data = [Scattergeo(lon=longs, lat=lats)]
#Otra forma de visualizar los datos, la facilidad es como agregas los atributos
data = [{
    "type": "scattergeo",
    "lon" : longs, 
    "lat" : lats,
    'marker' : {
        "size" : [7 * mag for mag in mags], #Lista de comprension para hacer mas grande la magnitud que es con lo que se esta graficando el tamanio de los puntos
        "color" : mags,
        "colorscale" : "Viridis",
        "colorbar" : {
            "title": "Magnitud"
        } ,
        "reversescale": True
    }
}]

my_layout = Layout(title = "Global Earthquakes")

fig = {"data":data, "layout": my_layout}

offline.plot(fig, filename="Ejercicios/Analisis_de_datos/json/global_eq.html")

