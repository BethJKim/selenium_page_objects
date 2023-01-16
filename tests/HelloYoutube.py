from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Ford", "Mustang", 2022, "Red")

print(car_2.make, car_2.model, car_2.year)
car_2.drive()
car_1.stop()
