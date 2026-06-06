class Car:

    __total_car_objects_created = 0

    def __init__(self, brand, model):
        Car.__total_car_objects_created += 1
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "petrol or diesel"

    @classmethod
    def get_total_car_object(cls):
        return cls.__total_car_objects_created

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

    def fuel_type(self):
        return "Electric charge"


my_car = Car("Toyota", "Fortuner")
print(f"Full name of car is : {my_car.get_details()}")
print(f"my car fuel type is : {my_car.fuel_type()}")

my_car = Car("Toyota", "Fortuner")
print(f"Full name of car is : {my_car.get_details()}")
print(f"my car fuel type is : {my_car.fuel_type()}")

ev = EV("a", "b", 300)
print(ev.get_ev_details())
print(f"ev car fuel type is : {ev.fuel_type()}")

ev = EV("a", "b", 300)
print(ev.get_ev_details())
print(f"ev car fuel type is : {ev.fuel_type()}")

print(f"Total car objects created till now are : {Car.get_total_car_object()}")
