
class Animal:
    def __init__(self, name):
        self.name=name
    def eat(self):
            return 'ест'

    def sleep(self):
            return "спит"
    
class Walker:
    def walk(self):
        return "ходит"
    
class Swimmer:
     def swim(self):
        return "плавает"
        
class Flyer:
    def fly(self):
        return "летает"

class Penguin(Animal,Walker,Flyer):
    def __init__(self, name):
        super().__init__(name)
    
    def describe(self):
        return f"{self.name} может {Walker.walk(self)} и {Flyer.fly(self)}"

class Duck(Animal, Walker, Swimmer, Flyer):
    def __init__(self, name):
         super().__init__(name)
    def describe(self):
        return f"{self.name} может {Walker.walk(self)}, {Swimmer.swim(self)} и {Flyer.fly(self)}"

class Bat(Animal, Flyer):
    def __init__(self, name):
        super().__init__(name)
    def describe(self):
        return f"{self.name} может {Flyer.fly(self)}"

dog=Animal("Собака")
cat=Animal("Кошка")
fish=Animal("Рыба")
eagle=Animal("Орёл")
walker=Walker()
swimmer=Swimmer()
flyer=Flyer()
penguin=Penguin("Пингвин")
duck=Duck("Утка")
bat=Bat("Летучая мышь")
print(f'''{cat.name} {cat.eat()} и {cat.sleep()}
{dog.name} {walker.walk()}
{fish.name} {swimmer.swim()}
{eagle.name} {flyer.fly()}

{penguin.describe()}
{duck.describe()}
{bat.describe()}''')