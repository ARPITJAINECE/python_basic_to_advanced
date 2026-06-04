class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car("Toyota", "Fortuner")
# print(my_car.brand, my_car.model)

print(f"Full name of car is : {my_car.full_name()}")
