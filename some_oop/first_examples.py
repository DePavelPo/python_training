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

# OOP Exercise 5: Define property that should have the same value for every class instance
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
class Vehicle:
    color = 'white'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

objBus5, objCar5 = Bus('School Volvo', 180, 12), Car('Audi Q5', 240, 18)
print('Color: ', objBus5.color, 'Vehicle name: ', objBus5.name, 'Speed: ', objBus5.max_speed, 'Mileage: ', objBus5.mileage)
print('Color: ', objCar5.color, 'Vehicle name: ', objCar5.name, 'Speed: ', objCar5.max_speed, 'Mileage: ', objCar5.mileage)

# OOP Exercise 6: Class Inheritance

# Create a Bus child class that inherits from the Vehicle class. 
# The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. 
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        return amount * 1.1

objBus6 = Bus('School Volvo', 12, 50)
print("Total Bus fare is: ", objBus6.fare())

# OOP Exercise 7: Determine which class a given Bus object belongs to (Check type of an object)
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

objBus7 = Bus("School Volvo", 12, 50)
print(type(objBus7))

# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

objBus8 = Bus("School Volvo", 12, 50)
print(isinstance(objBus8, Vehicle))