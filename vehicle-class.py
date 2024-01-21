#! /usr/bin/python3

# Note - initial class with only attributes (data)
# Base Class we've named Vehicle
class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

## 2 sub-classes - Car & Motorcycle
# the Car class derives/descends off the Vehicle class
class Car(Vehicle):
    def __init__(self, enginetype, carmanufacturer, carmodel):
        super().__init__("Car")
        self.wheels = 4
        self.doors  = 4
        self.enginetype = enginetype
        self.carmanufacturer = carmanufacturer
        self.carmodel = carmodel

    def drive(self, speed):
        super().drive(speed)
        print("Driving my ", self.carmanufacturer, self.carmodel,  self.enginetype, "car at", self.speed)

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

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)

# Creating instances/objects from the Classes
car1 = Car("diesel", "Toyota", "Celica")
car2 = Car("electric", "Honda", "Prius")
car3 = Car("petrol", "Toyota", "Lexus")
car4 = Car("hybrid", "Peugeot", "208i")

mc1 = Motorcycle("petrol", True)
mc2 = Motorcycle("petrol", False)


print("The current vehicle stock for PhunkyTech listed below: ")
print("Car1 has a " + car1.enginetype + " engine type")
print(car2.enginetype)
print(car3.enginetype)
print(car4.enginetype)

## We call those functions on the objects
car1.drive(20)
car2.drive(30)
car3.drive(45)
car4.drive(66)

mc1.drive(60)
mc2.drive(32)
