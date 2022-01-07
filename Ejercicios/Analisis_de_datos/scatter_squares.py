from matplotlib import pyplot

pyplot.style.use("seaborn")

x_values = list(range(1, 1000))
y_values = [x ** 2 for x in x_values]

fig, ax = pyplot.subplots()
#setting a solid color
#ax.scatter(x_values, y_values, c=(0,1,0), s=50) 
#setting a gradient color
ax.scatter(x_values, y_values, c=x_values, cmap=pyplot.cm.turbo, s=50)  #para el color los basicos se agregan como string pe "red", para uno customizado se agregan como tuplas
ax.set_title("Square numbers")
ax.set_xlabel("Value")
ax.set_ylabel("Square of value")

ax.tick_params(axis="both")

ax.axis([0, 1100, 0, 1_100_000])

pyplot.savefig("squares_plot.png", bbox_inches='tight')

pyplot.show()