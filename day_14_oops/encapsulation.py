class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand + " !"

    def get_details(self):
        return {
            "brand": self.__brand,
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


ev = EV("a", "b", 300)
print(ev.get_ev_details())

# print(f"Brand is : {ev.__brand}")

print(f"Brand is : {ev.get_brand()}")
