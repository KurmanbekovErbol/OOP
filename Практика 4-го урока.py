class Employee:
    def __init__(self,name,bid):
        self.name=name
        self.bid=bid

    def calculate_salary(self):
        self.bid=0
        return f'Зарплата по умолчанию: {self.bid} сомов'
    
    def display_info(self):
        return f'Имя сотрудника: {self.name}'
    
class FullTimeEmployee(Employee):
    def __init__(self, name, bid):
        super().__init__(name, bid)

    def calculate_salary(self):
        return f'Зарплата с фиксированным коэффициентом - {int(self.bid * 1.2)} сомов'
    
class PartTimeEmployee(Employee):
    def __init__(self, name, bid, time):
        super().__init__(name, bid)
        self.time=time * 0.5

    def calculate_salary(self):
        return f'Зарплата с отработанными часами - {int(self.bid * self.time)} сомов'
    
def process_salary(employee = Employee("Эрбол", 10000)):
    print(employee.calculate_salary())
    print(employee.display_info())

    order = [FullTimeEmployee("Данил", 10000), PartTimeEmployee("Вася", 10000,4)]
    for orders in order:
        print(orders.calculate_salary())
        print(orders.display_info())
    
process_salary()