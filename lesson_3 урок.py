"""Инкапсуляция"""

# Публичный класс
class PubliExample:
    def __init__(self, value):
        self.value=value  # Публичный атребут

    def info(self):
        return self.value
    
Public=PubliExample(32)
print(Public.info()) # Вызов публичного метода
print(Public.value) # Доступ к публичный атребуту

class ProtectedExample:
    def __init__(self, value):
        self._value=value # Защишонный атребут

    def _info(self):
        return self._value # Защишонный метод
    
protected=ProtectedExample(100)
print(protected._info()) # Это работает, но это противоречит принципам 
print(protected._value)  # Можно получить значение напрямую, но это не рекомендуется


class PrivateExample: # Приватный класс
    def __init__(self, value):
        self.__value=value # Публичный атребут

    def __info(self):
        return f"Привет класс {self.__value}" # Защишонный метод
    
    def access_private(self):
        return self.__info() # Публичный методб где мы получаем доступ к приватному методу или атрибуту
    
private=PrivateExample(555)

# Прямой вызов приватного метода вызовет ошибку
# print(private.__info())

# Прямой вызов приватного атребута вызовет ошибку
# print(private.__value)

# Доступ черес публичный метод
# print(private.access_private())

# Доступ к приватному атрибуту либо методу  черес name mangling
# print(private._PrivateExample__info())
import datetime
class Car:
    def __init__(self, marka, model, year, mileage):
        self.marka=marka
        self.model=model
        self.__year=year
        self.__mileage=mileage

    def info(self):
        return f"Марка - {self.marka}\nМодель - {self.marka}"
    
    def _calculate_age(self):
        current = datetime.datetime.now().year
        return f"Возраст машины - {current - self.__year}"
    
    def __update_mileage(self):
        return self.__mileage
    
    def set_mileage(self):
        return self.__update_mileage()
    
a=Car(1,2,3,4)
