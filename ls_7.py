# Напишите класс Subscriber, у которого есть переменные экземпляра:  firstname, lastname. Сделайте так, чтобы магический метод __str__ возвращал firstname + lastname. Создайте экземпляр класса и выведите данные их конструктора.

# class Subscriber:
#     def __init__(self,firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def __str__(self):
#         return self.firstname +" " + self.lastname

# subscriber = Subscriber("Surgabai","Kumavich")
# print(subscriber.__str__())



# class Car:
#     def __init__(self,make,model,year,):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometr = 0
#         self.fuel = 70

#     def __add_distance(self, distance):
#         self.odometer += distance

#     def __subtract_fuel(self, fuel):
#         self.fuel -= fuel

#     def drive(self, km):
#         fuel = km / 10
#         if self.fuel >= fuel:
#             self.__add_distance(km)
#             self.__subtract_fuel(fuel)
#             print("Lets drive!")
#         else:
#             print("Need more fuel, please, fill more")
              
# car = Car('Lexus', 'Lx570', 2019)
# car.drive(5000000)



# Создайте класс банковского счета для пользователя. В нем должен хранится баланс - количество средств на счету пользователя. У него должны быть методы пополнения и вычитания со счета. Так же создайте приватный параметр, в которой будет храниться некий налог на услугу вычета со счета пользователя. Не забудьте, что баланс не может быть отрицательным, то есть пользователь не может отнять от своих средств сумму больше чем его баланс. Создайте экземпляр этого класса с балансом на ваше усмотрение. Добавьте средств на баланс. Отнимите средства с баланс
