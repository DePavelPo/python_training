# OOP Exercise 1: Create a Vehicle class with max_speed and mileage instance attributes
class Vehicles:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

vehocleObj = Vehicles(190, 2400)
print('Max speed: ', vehocleObj.max_speed, '\nMileage: ', vehocleObj.mileage)

# OOP Exercise 2: Create a Vehicle class without any variables and methods
class Veshicle:
    pass

# OOP Exercise 3: Create a child class Bus that will inherit all 
# of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

busObj = Bus('School Volvo', 180, 12)
print('Vehicle Name: ', busObj.name, '\nSpeed: ', busObj.max_speed,
                 '\nMileage: ', busObj.mileage)

# OOP Exercise 4: Class Inheritance
# Create a Bus class that inherits from the Vehicle class. 
# Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Vehicle1:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus1(Vehicle1):
    def seating_capacity(self):
        return super().seating_capacity(capacity=50)

busWithCapacity = Bus1('School Volvo', 180, 12)
print(busWithCapacity.seating_capacity())