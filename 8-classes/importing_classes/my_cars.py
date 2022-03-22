from car import Car
from electric_car import EletricCar

my_beetle = Car("volkswagen", "beetle", 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EletricCar("tesla", "roadster", 2019)
print(my_tesla.get_descriptive_name())
