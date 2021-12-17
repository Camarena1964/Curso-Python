class Battery:
    def __init__(self, size, temperature):
        self.size = size #Value in KWh
        self.cycles = 0
        self.temperature = temperature

def describe_battery(self):
        print(f"This car has a {self.battery_size} KWh battery.")