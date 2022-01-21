import csv
import matplotlib.pyplot as plt
from datetime import datetime

#filename = "C:/Users/sandr/Desktop/Curso-Python/Ejercicios/Analisis_de_datos/CSV/Data/sitka_weather_07-2018_simple.csv"
filename =  'C:/Users/sandr/Desktop/Curso-Python/Ejercicios/Analisis_de_datos/CSV/Data/sitka_weather_2018.csv'
with open(filename) as file:
    reader = csv.reader(file)
    #header = next(reader)
    next(reader)
    
    #print(header)

    #date =datetime.strptime ('25/18/2018', '%d/%d/%Y) para convertir el formato de la fecha

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[-2])
        highs.append(high)
        low = int(row[-1])
        lows.append(low)
    print (highs)  

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates,  highs, c ='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
    ax.set_title('Daily high and temperatures , July 2018', fontsize = 24)
    ax.set_xlabel("")
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize = 15)


    plt.show()