class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def start():
        return "Транспортное средство заводится"

    def stop():
        return "Транспортное средство останавливается"
    
    def info(self):
        return f"Марка - {self.brand}, модель - {self.model}, год выпуска - {self.year} "
    
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors=doors
        print(f'{Vehicle.info(self)}, количество дверей - {self.doors}')
    
    def open_trunk():
        print("Багажник открыт")

    def start():
        print("Машина заводится")
    
    def stop():
        print("Машина останавливается")

class Bicycle(Vehicle):
    def __init__(self, brand, model, year, type_of_bicycle):
        super().__init__(brand, model, year)
        self.type_of_bicycle=type_of_bicycle
        print(f'{Vehicle.info(self)}, тип велосипеда - {self.type_of_bicycle}')

    def ring_bell():
        print("Звонок звенит")

    def start():
        print("Велосипед начинает движение")

    def stop():
        print("Велосипед останавливается")

class Boat(Vehicle):
    def __init__(self, brand, model, year, length):
        super().__init__(brand, model, year)
        self.length=length
        print(f'{Vehicle.info(self)}, длина лодки - {self.length}')

    def anchor():
        print("Якорь спущен")

    def start():
        print("Лодка отплывает")

    def stop():
        print("Лодка причаливает")

def all():
    vehicle=Vehicle("BMW","BMW 4 Series Gran Coupe","2014")
    print(f"{vehicle.info()}\n{Vehicle.start()}\n{Vehicle.stop()}")

    print()

    car=Car('Mercedes-Benz','CLA','2017','4')
    car.doors
    Car.open_trunk()
    Car.start()
    Car.stop()

    print()

    bicycle=Bicycle('STELS','Navigator 970 D 29','2021','горный')
    bicycle.type_of_bicycle
    Bicycle.ring_bell()
    Bicycle.start()
    Bicycle.stop()

    print()

    boat=Boat('ЛОDКИ ПИТЕR','ПВХ Triton AIR 330','2023','330 см')
    boat.length
    Boat.anchor()
    Boat.start()
    Boat.stop()
all()