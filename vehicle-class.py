#! /usr/bin/python3

# Note - initial class with only attributes (data)
# Base Class we've named Vehicle
class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

## 2 sub-classes - Car & Motorcycle
# the Car class derives/descends off the Vehicle class
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors  = 4
        self.enginetype = enginetype

# the Motorcycle class also derives/descends off the Vehicle class
class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

# Creating instances/objects from the Classes
car1 = Car("diesel")
car2 = Car("electric")
car3 = Car("petrol")
car4 = Car("hybrid")

mc1 = Motorcycle("petrol", True)
mc2 = Motorcycle("petrol", False)


print("The current vehicle stock for PhunkyTech listed below: ")
print("Car1 has a " + car1.enginetype + " engine type")
print(car2.enginetype)
print(car3.enginetype)
print(car4.enginetype)
