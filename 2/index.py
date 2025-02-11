# Обработка ошибок

# try-except:
# try:
# result = 10 / 0
# except ZeroDivisionError:
# print("Ошибка: деление на ноль!")

# Импорт модуля:
# import math
# print(math.sqrt(16))  # 4.0
# Импорт конкретной функции:
# from math import sqrt
# print(sqrt(25))  # 5.0

# В Python работа с файлами осуществляется с помощью встроенной функции open().
# Файлы можно открывать для чтения, записи или добавления данных.
# После работы с файлом его нужно закрыть, чтобы освободить ресурсы.
# Для этого используется метод close() или конструкция with, которая автоматически закрывает файл.

# "r" (read) — чтение (по умолчанию).
# "w" (write) — запись (если файл существует, он будет перезаписан).
# "a" (append) — добавление в конец файла.
# "b" (binary) — работа с бинарными файлами (например, "rb" или "wb").
# "+" — открытие для чтения и записи одновременно.

# Чтение из файла
# Открываем файл для чтения
# with open("example.txt", "r", encoding="utf-8") as file:
# content = file.read()  # Читаем весь файл
# print(content)

# with open(...) as file: — автоматически закрывает файл после завершения блока.
# file.read() — читает весь файл как строку.
# file.readline() — читает одну строку.
# file.readlines() — возвращает список строк.

# with open("example.txt", "w", encoding="utf-8") as file:
# file.write("Привет, мир!\n")
# file.write("Это пример записи в файл.")

# file.write() — записывает строку в файл.
# \n — символ новой строки.

# Пример добавления данных в конец файла:
# Открываем файл для добавления
# with open("example.txt", "a", encoding="utf-8") as file:
# file.write("\nДобавим еще одну строку.")

# Пример работы с файлом
# Запись в файл
# with open("data.txt", "w", encoding="utf-8") as file:
# file.write("Первая строка\n")
# file.write("Вторая строка\n")
# Чтение из файла
# with open("data.txt", "r", encoding="utf-8") as file:
# for line in file:  # Читаем файл построчно
# print(line.strip())  # strip() убирает лишние пробелы и символы новой строки


# ООП — это подход к программированию, основанный на концепции объектов.
# В Python всё является объектами, и ты можешь создавать свои собственные
# типы данных с помощью классов.
# Основные концепции ООП
# Класс — это шаблон для создания объектов. Он определяет
# свойства (атрибуты) и методы (функции) объекта.
# Объект — это экземпляр класса.
# Атрибуты — переменные, которые принадлежат объекту.
# Методы — функции, которые принадлежат объекту.
# Конструктор — метод __init__, который вызывается при создании объекта.

# Пример класса
# Создаем класс Person
# class Person:
# Конструктор (инициализирует объект)
# def __init__(self, name, age):
# self.name = name  # Атрибут name
# self.age = age    # Атрибут age

# Метод для приветствия
# def greet(self):
# return f"Привет, меня зовут {self.name}, мне {self.age} лет."

# Создание объекта
# Создаем объект класса Person
# person = Person("Alice", 25)
# Вызываем метод greet
# print(person.greet())  # Привет, меня зовут Alice, мне 25 лет.

# Наследование
# Наследование позволяет создавать новый класс на основе существующего.
# Новый класс (дочерний) наследует атрибуты и методы родительского класса.
# Пример:
# Родительский класс
# class Animal:
# def __init__(self, name):
# self.name = name
# def speak(self):
# return "Звук животного"
# Дочерний класс
# class Dog(Animal):
# def speak(self):
# return "Гав!"

# Создаем объект дочернего класса
# dog = Dog("Бобик")
# print(dog.speak())  # Гав!


# Инкапсуляция
# Инкапсуляция — это сокрытие внутренней реализации объекта.
# В Python нет строгой инкапсуляции, но принято обозначать "приватные" атрибуты с
# помощью префикса _.
# Пример:
# class BankAccount:
# def __init__(self, balance):
# self._balance = balance  # "Приватный" атрибут

# def deposit(self, amount):
# self._balance += amount

# def get_balance(self):
# return self._balance

# account = BankAccount(100)
# account.deposit(50)
# print(account.get_balance())  # 150

# Полиморфизм
# Полиморфизм позволяет использовать объекты разных классов одинаковым образом.
# Пример:
# class Cat(Animal):
# def speak(self):
# return "Мяу!"
# Функция, которая работает с любым объектом, у которого есть метод speak
# def animal_sound(animal):
# print(animal.speak())
# Создаем объекты
# dog = Dog("Бобик")
# cat = Cat("Мурзик")
# Вызываем функцию
# animal_sound(dog)  # Гав!
# animal_sound(cat)  # Мяу!

# Пример ООП: класс Rectangle
# class Rectangle:
# def __init__(self, width, height):
# self.width = width
# self.height = height
# def area(self):
# return self.width * self.height

# def perimeter(self):
# return 2 * (self.width + self.height)

# Создаем объект
# rect = Rectangle(5, 10)
# print("Площадь:", rect.area())  # Площадь: 50
# print("Периметр:", rect.perimeter())  # Периметр: 30

