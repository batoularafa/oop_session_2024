# Base class: Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"

    def honk(self):
        print("Honk honk!")

# Inherited class: Car
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def description(self):
        return f"{super().description()} with {self.doors} doors"

    def honk(self):
        print("Beep beep!")

# Inherited class: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_size):
        super().__init__(make, model, year)
        self.engine_size = engine_size

    def description(self):
        return f"{super().description()} with {self.engine_size}cc engine"

    def honk(self):
        print("Vroom!")

# Inherited class: Truck
class Truck(Vehicle):
    def __init__(self, make, model, year, bed_size):
        super().__init__(make, model, year)
        self.bed_size = bed_size

    def description(self):
        return f"{super().description()} with {self.bed_size}ft bed"

    def honk(self):
        print("HONK HONK!")

# Create instances of each vehicle type
my_car = Car("Toyota", "Corolla", 2015, 4)
my_motorcycle = Motorcycle("Harley-Davidson", "Softail", 2018, 1200)
my_truck = Truck("Ford", "F-150", 2020, 6.5)

# Demonstrate polymorphism
vehicles = [my_car, my_motorcycle, my_truck]

for vehicle in vehicles:
    print(vehicle.description())
    vehicle.honk()
    print()