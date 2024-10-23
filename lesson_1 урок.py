class car:
    def __init__(self, wheel, motor, body):
        self.wheel=wheel
        self.motor=motor
        self.body=body

        self.bak=20
        self.is_start=False

    def info(self):
        print(f"Колесо - {self.wheel}, Мотор - {self.motor}, Кузов - {self.body}")

    def start(self):
        if self.bak > 0:
            self.is_start = True
            print(f"Машина заведена")
        else:
            print("У машины нет топливо")

    def stop(self):
        self.is_start = False
        print("Машина заглушена")

    def drive(self, city):
        if self.is_start == True:
            print(f"Машина едет в {city}")
        else:
            print("Машина не заведена")

car = car("R20","V8","Sedan")
car.info()
car.start()
car.stop()
car.drive("Дубай")

name = ("Asko", "Isko", "Sema")
name_1=list(name)
name_1.append("Erbol")
name = tuple(name_1)
print(name)

class book:
    def __init__(self, avtor, book_name, year):
        self.avtor=avtor
        self.book_name=book_name
        self.year=year
    def info(self):
        print(f"Автор - {self.avtor}\nНазвание книги - {self.book_name}\nДата выпуска книги - {self.year}")
book = book("Льва Николаевича Толстого","Вайна и мир","1867")
book.info()