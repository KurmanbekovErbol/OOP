#1)
class Fruits:
    def __init__(self, name, color, weight):
        self.name=name
        self.color=color
        self.weight=weight
    def fruit(self):
        print(f"Название - {self.name}\nЦвет - {self.color}\nВес - {self.weight} грамм\n")
fruit_apple=Fruits("яблоко","красный,желтый,зелёный","150")
fruit_lemon=Fruits("лимон","желтый","120")
fruit_banana=Fruits("банан","желтый","180")
fruit_apple.fruit()
fruit_lemon.fruit()
fruit_banana.fruit()
#=========================================================================================================
#2)
class Book:
    def __init__(self, title, author, pages):
        self.title=title
        self.author=author
        self.pages=pages
    def check_pages(self):
        if int(self.pages) < 100:
            print("Тонкая книга")
        elif 100 <= int(self.pages) <= 300:
            print("Средняя книга")
        elif 300 < int(self.pages):
            print("Толстая книга")
    def info(self):
        print(f"Название - {self.title}\nАвтор - {self.author}\nКоличество страниц - {self.pages}")
Book = Book("Вайна и мир","Льва Николаевича Толстого","1300")
Book.info()
Book.check_pages()