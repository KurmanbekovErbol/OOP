import random
number_of_attempts = int(input("Сколько количество попыток вы хотите?:"))
number = random.randint(1,101)
while number_of_attempts > 0:
    search = int(input("Введите число:"))
    if search > number:
        print("Меньше")
    elif search < number:
        print("Больше")
    elif search == number:
        print("Вы угадали число")
        break
    number_of_attempts -= 1
if number_of_attempts == 0:
    print("Попытки закончились")