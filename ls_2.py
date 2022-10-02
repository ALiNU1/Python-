# name = "Muntasir" #публичный
# _name = "Muntasir" #защищеный
# __name = "Muntasir" #приватнный

# class Phone:
#     def __init__(self, brand, model, year, color):
#         self.brand = brand 
#         self.model = model 
#         self.year = year 
#         self.color = color 
#         self.__battery = 100 

#     def use(self):
#         print("Телефон заряжется")
#         self.__battery_use()

#     def __battery_use(self):
#         self.__battery -= 1 
#         print("Зарядка пошла и минус один процент")

#     def __battery_add(self):
#         self.__battery += 1


#     def info_phone(self):
#         print(f"{self.brand} {self.model} {self.__battery}")

# phone = Phone("Iphone", "13", 2021, "White")
# phone.use()
# phone.use()
# phone.use()
# phone.use()
# phone.info_phone()
# phone.__battery = 100
# print(phone.__battery)
# phone.info_phone()

# class Kettle:
#     def __init__(self, brand, model, color):
#         self.brand = brand 
#         self.model = model 
#         self.color = color
#         self.__number = 10

#     def turn_on(self):
#         print("Чайник включился")
#         self.__booll()
#         self.__check_temperature()
#         self.__beep()
#         self._turn_off()

#     def __booll(self):
#         print("Разогрев воды")

#     def __check_temperature(self):
#         print("Проверка температуры воды")

#     def __beep(self):
#         print("Сигнал что вода нагрета")

#     def _turn_off(self):
#         print("Автоматическое выключение")

# kettle = Kettle("Chainik", "Python", "White")
# print(kettle._Kettle__number)
    