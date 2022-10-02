# class HelloWorld:
#     pass

# print(type(HelloWorld))


# class Dog:
#     name = 'surgabai'
#     age = 14
#     color = 'ne White'

#     def gaw(self):
#         print("Gaw")

#     def fas(self):
#         print("Кусь-Кусь")


# dog = Dog()
# print(dog.name)
# dog.gaw()
# dog.fas()

# class Dog:
#     def  __init__(self,name,age,color):
#         self.name = name
#         self.age = age
#         self.color = color 

#     def gaw(self):
#         print("Gaw")

#     def fas(self):
#         print("Кусь-Кусь")

#     def info(self):
#         print(f"Name:{self.name},age:{self.age},color:{self.color}")

# dog1 = Dog("Surgabai",14,"Не White")
# dog1.gaw()
# dog1.fas()

# dog2 = Dog("Barsik",10,"Black")
# dog2.gaw()
# dog2.info()

# class Hello:
#     def say_hello(self):
#         print("Alinur")

# hello = Hello()
# hello.say_hello()

# class Car:
#     def __init__(self,brend,model,type_body,year,volume,color):
#         self.brend = brend
#         self.model = model
#         self.type = type_body
#         self.year = year
#         self.volume = volume
#         self.color = color
#         self.odometr = 0
#         self.is_going = False

#     def info_car(self):
#         return f"{self.brend},{self.model},{self.year},{self.odometr} km, status {self.is_going}"

#     def car_is_going(self,km):
#         self.odometr += km
#         self.is_going = True

#     def stop_car(self):
#       if self.is_going = False:
        #     return f"Ваш мотор не заведен"
        # elif self.is_going = True:
        #     self.is_going = False

# bmw = Car("Lada","Жигули","Kupe",2017,"3.6","Purple")
# print(bmw.info_car())
# bmw.car_is_going(100)
# print(bmw.info_car())
# bmw.car_is_going(100)
# bmw.car_is_going(100)
# bmw.car_is_going(100)
# print(bmw.info_car())
# bmw.stop_car()
# print(bmw.info_car())

# print("============")

# audi = Car("Audi", "A8", "Sedan", 2021, "3.5", "Black")
# print(audi.info_car())
# audi.car_is_going(500)
# print(audi.info_car())
# audi.stop_car()
# print(audi.info_car())

# 1) Напишите класс Cow, создайте метод make_sound, который выводит на экран
# “Мууу!”. Создайте экземпляр, вызовите метод make_sound

# class Cow:
#     def make_sound(self):
#         print("Мууу")

# cow = Cow()
# cow.make_sound()

# 2) Создайте класс Cars, у которого есть переменные экземпляра:
# brand, model, year, odometer, type_of, volume, is_going = False. Создайте метод info_about_car который выводит переменные экземпляра brand, model и year. Затем создать метод car_is_going, который принимает аргумент km. Внутри этого метода добавляем в odometer += km 
# который мы передаем через аргумент, делаем is_going = True и возвращаем odometer и is_going. Потом пишем еще один метод car_not_going. Внутри этого метода мы делаем is_going = False и возвращаем его. 
# В конце создайте экземпляр и вызовите все методы.

# class Car:
#     def __init__(self,brend,model,type_body,year,volume,color):
#         self.brend = brend
#         self.model = model
#         self.type = type_body
#         self.year = year
#         self.volume = volume
#         self.color = color
#         self.odometr = 0
#         self.is_going = False

#     def info_car(self):
#         return f"{self.brend},{self.model},{self.year},{self.odometr} km, status {self.is_going}"

#     def car_is_going(self,km):
#         self.odometr += km
#         self.is_going = True

#     def stop_car(self):
#         self.is_going = False

# bmw = Car("Lada","Жигули","Kupe",2017,"3.6","Purple")
# print(bmw.info_car())
# bmw.car_is_going(100)
# print(bmw.info_car())
# bmw.car_is_going(100)
# bmw.car_is_going(100)
# bmw.car_is_going(100)
# print(bmw.info_car())
# bmw.stop_car()
# print(bmw.info_car())

# 3) Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекта:  make (марка), model, year, max_speed, odometer, is_flying и 
# методы имитирующих поведение самолета take_off (взлет), fly (летать), land
# приземление), info_about_fly(информация об полете), info_about_plane(информация об самолете). 
# Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

# class Airplane:
#     def __init__(self,mark,model,year,max_speed):
#         self.mark = mark
#         self.model = model
#         self.max_speed = max_speed
#         self.year = year
#         self.odometr = 0
#         self.is_flying = False
#         self.take_off = False
#         self.fly = True
#         self.land = True

#     def info_car(self):
#         return f"{self.mark},{self.model},{self.year},{self.max_speed},{self.odometr} km,"


# from time import sleep


# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']

#     def running(self):
#         i = 0
#         while i != 3:
#             print(TrafficLight.__color[i])
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(5)
#             i += 1


# t = TrafficLight()
# t.running()