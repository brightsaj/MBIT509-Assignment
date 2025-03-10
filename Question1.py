# Base class Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        return f"Driving a generic {self.brand} {self.model}."

# Subclass Car
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def drive(self):
        return f"Driving a {self.brand} {self.model} car with {self.num_doors} doors."

# Subclass Bike
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def drive(self):
        return f"Riding a {self.brand} {self.model} {self.bike_type} Bike."

# Example usage
print(Vehicle("Generic", "Vehicle").drive())  # Output: Driving a generic Generic Vehicle.
print(Car("Toyota", "Landcruiser", 4).drive())    # Output: Driving a Toyota Landcruiser car with 4 doors.
print(Bike("Trek", "Premium", "Mountain").drive())  # Output: Riding a Trek Mountain Mountain bike.