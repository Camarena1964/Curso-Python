from Carro import Car
from Ejercicios.POO.Battery import Battery

class ElectricCar(Car):

    def __init__(self, trademark, model, year):
        super().__init__(trademark, model, year)
        self.battery_size = 75 #Value in KWh
        self.bettery_cycles = 0
        self.battery_temperature = 0
    
    def fill_gas_tank(self):
        print("This is an electric car, you dont need to fill the tank")   #Ojo se sobreescribio el metodo

my_tesla = ElectricCar("Tesla", "S", 2020)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

# class FlyElectricCar(ElectricCar):        no lo alcance a copiar, pero se pueden crear clases de subclases
#     def __init__(self, trademark, model, year):
#         super().__init