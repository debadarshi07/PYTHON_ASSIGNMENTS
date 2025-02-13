class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle Make: {self.make}")
        print(f"Vehicle Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")

vehicle = Vehicle("Maruti", "Alto")
vehicle.display_info()

print("\n")

car = Car("Maruti", "800", 4)
car.display_info()