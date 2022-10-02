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


# class Student:
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname

#     def __str__(self):
#         return f" Str {self.name} {self.surname}"

#     def __repr__ (self):
#         return f"Repr {self.name} {self.surname}"

#     def __call__(self):
#         return "Call"

# student = Student("alinur","IT")
# print(student)
# print(student())

# class Car:
#     def __init__(self,brand,model,price):
#         self.brend = brand
#         self.model = model
#         self.price = price

#     def __str__(self):
#         return f"{self.brend} ,{self.model} ,{self.price}"

#     def __eq__(self,car):
#         self.price == car.price


# bmw = Car("BMW","I8",8000000)
# print(bmw)
# lexus = Car("Lexus","LX570",700000)
# print(lexus)
# print(bmw == lexus)
