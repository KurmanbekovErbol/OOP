class Animal:
    def make_sound():
        pass
    
    def display_info():
        pass
    def __init__(self, name, age):
        self.name=name
        self.age=age



class Lion(Animal):
    def make_sound(self):
        print("Pppp!")

    def display_info(self):
        print(f"""Название - {self.name}, возраст - {self.age}
Лев - вид хищных млекопитающих, один из пяти представителей рода пантер,
относящегося к подсемейству больших кошек в составе семейства кошачьих.""")

class Elephant(Animal):
    def make_sound(self):
        print("Уууу!")

    def display_info(self):
        print(f"""Название - {self.name}, возраст - {self.age}
Слоновые, или слоны, — семейство класса млекопитающих из отряда хоботных. 
В настоящее время к этому семейству относятся 3 ныне живущих вида.""")
        
def introduce_animal(animal=Animal):
    animal.make_sound()
    animal.display_info()

    animal = [Lion("Лев", 10), Elephant("Слон", 60)]
    for animals in animal:
        animals.make_sound()
        animals.display_info()

introduce_animal()