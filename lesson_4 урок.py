""" Полиморфизм """

# num1 = 1
# num2 = 2
# print(num1 + num2)

# string1 = "Hello"
# string2 = "Geeks"
# print(string1 + string2)

#========================================================================================

# class Cat:
#     def __init__(self, name, preferences):
#         self.name=name
#         self.preferences=preferences

#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мне {self.preferences} года")

#     def make_sound(self):
#         print("Мяу!")

# class Dog:
#     def __init__(self, name, preferences):
#         self.name=name
#         self.preferences=preferences

#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мне {self.preferences} года")

#     def make_sound(self):
#         print("Гаф!")

# cat = Cat("Васька", 2)
# dog = Dog("Мухтар", 3)

# for animal in (cat, dog):
#     animal.make_sound()
#     animal.info()

#==================================================================================

# class PaymetMethot:
#     def pay(self, amount):
#         pass

# class CreditCart(PaymetMethot):
#     def pay(self, amount):
#         return f'Сумма {amount}, оплачивается по кредитной карты'
    
# class PayPal(PaymetMethot):
#     def pay(self, amount):
#         return f'Сумма {amount}, оплачивается PayPal'
    
# class BankTranfel(PaymetMethot):
#     def pay(self, amount):
#         return f'Сумма {amount}, оплачивается по банковскому переводу'
    
# payments = [CreditCart(), PayPal(), BankTranfel()]

# for payment in payments:
#     print(payment.pay(100))

#==============================================================================

class Vehicle:
    def start_engine(self):
        pass

    def stop_engine(self):
        pass

    def drive(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return 'Двигатель автомобиля заведён'
    
    def stop_engine(self):
        return 'Двигатель автомобиля не заведён'
    
    def drive(self):
        return 'Автомобил едет'
    
class Bycycle(Vehicle):
    def start_engine(self):
        return 'У велосипеда нет двигателя'
    
    def stop_engine(self):
        return 'У велосипеда нет двигателя'
    
    def drive(self):
        return 'Велосипед едет'
    
vehicle = [Car(), Bycycle()]

for vehicles in vehicle:
    print(vehicles.start_engine())
    print(vehicles.stop_engine())
    print(vehicles.drive())