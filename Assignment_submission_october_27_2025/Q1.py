# easy_car_class.py

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Car: {self.make} {self.model}"


# Example usage
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.display_info())
print(car2.display_info())
