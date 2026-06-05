class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def get_details(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "full_name": self.full_name(),
        }


class EV(Car):
    def __init__(self, brand, model, range):
        super().__init__(brand, model)
        self.range = range

    def get_ev_details(self):
        details = super().get_details()
        details["range"] = self.range
        return details


my_car = Car("Toyota", "Fortuner")
# print(my_car.brand, my_car.model)

# print(f"Full name of car is : {my_car.full_name()}")

ev = EV("a", "b", 300)
print(ev.get_ev_details())


my_tesla = EV("tesla", "model-a", 1500)

print(f"{isinstance(my_tesla, Car)}")
print(f"{isinstance(my_tesla, EV)}")
