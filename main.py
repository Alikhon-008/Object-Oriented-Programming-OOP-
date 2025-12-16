# print(type(2))
# print(isinstance(2, str))
# print(isinstance(2, int))
# print(dir('Good'))
# print(dir(5))
# print(f"lorem ipsum dolor sit amet"
#       f"LOREM ipsum dolor sit amet\n\n"
#       f"LOREM ipsum dolor sit amet\n"
#       f"LOREM ipsum dolor sit amet")


# class Animals:
#     animal = "Lion"
#     speed = "65 km/h"
#     weight = "150-250 kg"
#     gender = "Male"
#
# a = Animals()
# print(a.animal, a.speed, a.weight, a.gender)
# print(a.animal, a.weight)


# class Person:
#     def __init__(self, name, age, birth, country, work):
#         self.name = name
#         self.age = age
#         self.birth = birth
#         self.country = country
#         self.work = work
#
#     def person(self):
#         print(f"Ismi: {self.name}, Yoshi: {self.age}\n"
#               f"Tug'ilgan yili: {self.birth}\n"
#               f"Yashash joyi: {self.country}\n"
#               f"Ish joyi: {self.work}\n")
#
# person_1 = Person("John", "24", "September 21th", "Italy", "Police")
# person_2 = Person("Vera", "27", "January 21st", "USA", "Bodyguardian")
# # person_1.person()
# # person_2.person()
#
#
# class Student(Person):
#     def __init__(self, name, age, birth, country, work, learn):
#         super().__init__(name, age, birth, country, work)
#         self.learn = learn
#
#     def student(self):
#         print(f"Ismi: {self.name}, Yoshi: {self.age}\n"
#               f"Tug'ilgan yili: {self.birth}\n"
#               f"Yashash joyi: {self.country}\n"
#               f"Ish joyi: {self.work}\n"
#               f"Uqiydi: {self.learn}\n")
#
# student = Student('Amir', '19', 'August 21st', "Uzbekistan", 'part-time job', 'Management')
# student.student()



# EXAMPLE

# class HP:
#     def __init__(self, brand, weight, ram):
#         self.brand = brand
#         self.weight = weight
#         self.ram = ram
#
#     def laptop(self):
#         print(f"Laptop: {self.brand}\n"
#               f"Weight: {self.weight}\n"
#               f"Ram: {self.ram}")
#
# laptop_1 = HP('HP', '1.25 kg', '16 GB')
# laptop_1.laptop()
#
#
# class Asus(HP):
#     def __init__(self, brand, weight, ram, memory):
#         super().__init__(brand, weight, ram)
#         self.memory = memory
#
#     def laptop(self):
#         print(f"Laptop: {self.brand}\n"
#               f"Weight: {self.weight}\n"
#               f"Ram: {self.ram}\n"
#               f"Memory: {self.memory}")
#
# laptop_2 = Asus('Asus', '1.25 kg', '16 GB', "500 GB")
# laptop_2.laptop()