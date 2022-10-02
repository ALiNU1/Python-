# from abc import ABC,abstractclassmethod


# class Math:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     @abstractclassmethod
#     def add(self):
#         pass

#     @abstractclassmethod
#     def sub(self):
#         pass

#     @abstractclassmethod
#     def mult(self):
#         pass

#     @abstractclassmethod
#     def div(self):
#         pass

# class AbcMath(Math):
#     def __init__ (self,a,b):
#         super().__init__(a,b)

#     def add(self):
#         print(self.a + self.b)

#     def sub(self):
#         print(self.a - self.b)

#     def mult(self):
#         print(self.a * self.b)

#     def div(self):
#         print(self.a / self.b)

# math = AbcMath(10,10)
# math.add()
# math.sub()
# math.mult()
# math.div()

# import random
# print(random.randint(1,100))
# print(random.randrange(1,100,2))

# names = ["Alinur","Surgabai","Uulbu","Uluk","Muntasir"]
# print(random.choice(names))

# random_num = random.randint(1,10)
# n = 0
# while True:
#     find_num = int(input("Введите число: "))
#     if find_num >= 1 and find_num <=10:
#         n +=1
#         if n == 5:
#             print("У вас нет попыток(")
#             break
#         if find_num == random_num:
#             print("Вы выиграли")
#             break
#         else:
#             print(f"Неверно {5-n} попыток")
#     else:
#         print("Введите число от 1-10")

# Напишите класс Subscriber, у которого есть переменные экземпляра:  firstname, lastname. Сделайте так, чтобы магический метод __str__ возвращал firstname + lastname. Создайте экземпляр класса и выведите данные их конструктора.

# class Subscriber:
#     def __init__(self,firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def __str__(self):
#         return self.firstname +" " + self.lastname

# subscriber = Subscriber("Surgabai","Kumavich")
# print(subscriber.__str__())
