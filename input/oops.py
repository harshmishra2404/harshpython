# to map the real world scenarios, we started using objects in code
# This is called OOP
# class is a blueprint of creating object

# class car:
#     color="blue"
#     brand="BMW"
#
# car1=car()
# print(car1.brand)
# print(car1.color)

# car---->class name
# car1--->object

# CONSTRUCTOR:
# All classes have a function called __init__() which is always executed when the object is being initiated

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#
# my_car = Car("TATA", "NEXON")
# print(my_car.brand)
# print(my_car.model)
#
# my_new_car = Car("BMW", "M3")
# print(my_new_car.brand)
# print(my_new_car.model)


class Car:
    total_car = 0

    def __init__(self, brand, model,):
        self.brand = brand
        self.model = model
        Car.total_car = Car.total_car + 1

    def get__brand(self):
        return self.brand

    def fullname(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "petrol or diesel"

    @staticmethod
    def general__description():
        return "Cars are means of transport"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fullname(self):
        return f"{self.brand} {self.model} {self.battery_size}"

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Brand=Tesla", "Model=S", "Battery_size=85kwh")
my_car = Car("TATA", "NEXON")
my_new_car = Car("TOYOTA", "SUPRA")
Safari_car = Car("TATA", "SAFARI")
Ola_bike = ElectricCar("Brand=OLA", "Model=S", "Battery-Size=100Kwh")

print(my_tesla.fullname())
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)
print(my_tesla.fuel_type())
print()
print(my_car.fullname())
print(my_car.brand)
print(my_car.model)
print(my_car.fuel_type())
print()
print(my_new_car.fullname())
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.fuel_type())
print()
print(Safari_car.fullname())
print(Safari_car.brand)
print(Safari_car.model)
print(Safari_car.fuel_type())
print()
print(Ola_bike.fullname())
print(Ola_bike.brand)
print(Ola_bike.model)
print(Ola_bike.battery_size)
print(Ola_bike.fuel_type())
print()
print("Total no. of car= ", Car.total_car)
print()
print(Car.general__description())


# class student:
#     def __init__(self,fullname):
#         self.name=fullname
#
# s1=student("Harsh Mishra")
# print(s1.name)
#
# s2=student("karan upadhya")
# print(s2.name)