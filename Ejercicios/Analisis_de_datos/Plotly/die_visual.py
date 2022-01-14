from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#The 6 sides die

die = Die()

#forma 1
# results = []
# for _ in range (100):
#     results.append(die.roll())

#Forma 2: Lista de comprension
results = [die.roll() for _ in range (100)]
#print (results)

frequencies = []
for value in range(1, die.num_sides + 1):
    #pudo ser tambien range (die.num_sides) y agregar una linea abajo que diga values +1
    frequency = results.count(value)
    frequencies.append(frequency)

#print (frequencies)

x_values = list (range (1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title' : 'Result'}
y_axis_config = {'title' : 'Frequency of results'}

layout = Layout(title='Result of rolling one die 100 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout':layout}, filename = 'dieFrequencies.html')