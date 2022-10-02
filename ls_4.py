# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         return f"Name {self.name}, age {self.age}"

#     def sound(self):
#         return f"Gaww"

# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         return f"Name {self.name}, age {self.age}"

#     def sound(self):
#         return f"uwu"

# class Cow:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         return f"Name {self.name}, age {self.age}"

#     def sound(self):
#         return f"Muuu"

# dog = Dog("Surgabai",14)
# # print(dog.info())
# # print(dog.sound())

# cat = Cat("Surgabai",14)
# # print(cat.info())
# # print(cat.sound())

# cow = Cow("Surgabai",14)
# # print(cow.info())
# # print(cow.sound())

# for animal in (dog,cat,cow):
#     print(animal.info())
#     print(animal.sound())

# class Adidas:
#     def calc(self,a,b):
#         return a+b

# class Sub:
#     def calc(self,a,b):
#         return a-b

# class Mult:
#     def calc(self,a,b):
#         return a*b

# class Div:
#     def calc(self,a,b):
#         return a/b

# add = Adidas()
# sub = Sub()
# mult = Mult()
# div = Div()
# for i in (add,sub,mult,div):
#     print(i.calc(10,10))

# Напишите программу с классом Student, в котором есть три атрибута: name, 
# groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A. 
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, 
# setGroupNumber. Метод getName нужен для получения данных об имени конкретного 
# студента, метод getAge нужен для получения данных о возрасте конкретного студента, 
# vетод setGroupNumberнужен для получения данных о номере группы конкретного студента. 
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод 
# setGroupNumber позволяет изменить номер группы установленный по умолчанию. В программе 
# необходимо создать пять экземпляров 
# класса Student, установить им разные имена, возраст и номер группы.

# class Student:
#         def __init__(self,name = "Alinur", groupNumber = "8D",age = 13):
#            self.name = name
#            self.groupNumber = groupNumber
#            self.age = age

#         def getName(self):
#             return f"Name:{self.name}"

#         def getGroupNumber(self):
#             return f"Groupnumber:{self.groupNumber}"

#         def getAge(self):
#             return f"Age:{self.age}"

#         def setNameAge(self,name,age):
#             self.name = name 
#             self.age = age
          

#         def setGroupNumber(self,groupNumber):
#             self.groupNumber = groupNumber
#             return self.groupNumber

# student = Student()
# print(student.getAge())
# student.setNameAge("Ivan", 15)
# print(student.name)
# print(student.age)

# Описание: 
# Есть Алфавит, характеристиками которого являются: 
# 1. Язык
# 2. Список букв

# Для Алфавита можно: 
# 1. Напечатать все буквы алфавита
# 2. Посчитать количество букв

# Также есть Английский алфавит, который обладает следующими свойствами: 
# 1. Язык
# 2. Список букв
# 3. Количество букв

# Для Английского алфавита можно: 
# 1. Посчитать количество букв
# 2. Определить, относится ли буква к английскому алфавиту
# 3. Получить пример текста на английском языке

# Инструкция:
# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 
# 1) lang - язык и
# 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите

# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). 
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, 
# состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв 
# в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра 
# и определять, относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе 
# классе он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.

# Тесты:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке

# import string
# result = string.ascii_lowercase
# print(result)
# class Alphabet:
#     def __init__(self,lang,letter):
#         self.lang = lang
#         self.letter = letter
    
#     def print(self):
#         return self.letter

#     def letter_num(self):
#         return len(self.letter)

# class EngAlphabet(Alphabet):
    
#     _letter_num = 26

#     def __init__(self):
#         super().__init__('En',string.ascii_uppercase)

#     def is_en_letter(self,letter):
#         if letter.upper() in self.letter:
#             return f"Это буква есть в алфавите"
#         else:
#             return f"Такого нет"

#     def letter_num(self):
#         return EngAlphabet._letter_num

#     @staticmethod
#     def example():
#         print("Hello World")


# alphabet = EngAlphabet()
# print(alphabet.print())
# print(alphabet.letter_num())
# print(alphabet.is_en_letter("a"))
# print(alphabet.is_en_letter("й"))
# print(alphabet.example())
        
# class Tomato:
#     states = {0: 'Отсутствует', 1: 'Цветение', 2 : 'Зеленый', 3: 'Красный'}

#     def __init__(self, index):
#         self._index = index 
#         self._state = 0

#     def grow(self):
#         self._change_state() 

#     def _change_state(self):
#         if self._state < 3:
#             self._state += 1
        

#     def is_ripe(self):
#         if self._state == 3:
#             return "Созрел"
#         else:
#             return "Не созрел"

# class TomatoBush:
#     def __init__(self, num_tomato):
#         self.tomatoes = [Tomato(index) for index in range(0,num_tomato )]

#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()

#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes]) 

#     def give_away_all(self):
#         self.tomatoes = []

# class Gardener:
#     def __init__(self, name, plant):
#         self.name = name 
#         self._plant = plant 

#     def work(self):
#         self._plant.grow_all()
#         return "Садовник работает"
    
#     def harvest(self):
#         if self._plant.all_are_ripe():
#             self._plant.give_away_all()
#             return f"Плоды созрели и содовник собрал урожай"
#         else:
#             return f"Плоды не созрели"

#     @staticmethod
#     def knowledge_base():
#         return f"Справка по рукодству"

# print(Gardener.knowledge_base())
# tomato_bush = TomatoBush(4)
# sadovnik = Gardener("Maks", tomato_bush)
# print(sadovnik.work())
# print(sadovnik.work())
# print(sadovnik.work())
# print(sadovnik.work())
# print(sadovnik.harvest())