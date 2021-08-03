# class Person:
#     lang = 'English'

#     # __init__ is working like a constructor in other lang.
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     # self is instance obj. It must be provided other wise method doesn't work perfectly
#     def get_summary(self):
#         return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

# ps = Person('John Doe', 25, 'Male')    
# print(ps) # Output: <__main__.Person object at 0x7ff86530b040>
# print(ps.__dict__) # Output: {'name': 'John Doe', 'age': 25, 'gender': 'Male'}
# print(ps.name) # John Doe
# print(ps.lang) # English
# print(ps.get_summary()) # Output: Name: John Doe, Age: 25, Gender: Male


# Let's create a Setter & Getter of 'age' property in Person Class
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.__age = age # private class property
#         self.gender = gender

#     def get_age(self):
#         return self.__age

#     def set_age (self, age):
#         self.__age = int(age)

#     def get_summary(self):
#         return f"Name: {self.name}, Age: {self.__age}, Gender: {self.gender}"

# ps = Person('Justin Austin', 32, 'Male')   
# print(ps.get_age()) # Output: 32
# print(ps.name) # Output: Justin Austin

# # If explicitly call the private attribute like public, It must be displayed an Error. For Ex:
# print(ps.__age)
# # Output:
# # Traceback (most recent call last):
# #   File "Program/oop.py", line 45, in <module>
# #     print(ps.__age)
# # AttributeError: 'Person' object has no attribute '__age'

# print(ps._Person__age) # Output: 32 ->Note: It's not propessional

# Inheritance
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def get_area(self):
        return self.height * self.width

class Square(Rectangle):
    def __init__(self, size):
        self.size = size

    def get_area(self):
        return self.size * self.size

rc = Rectangle(5, 4)
print(rc.get_area()) # Output: 20

sq = Square(5)
print(sq.get_area()) # Output: 25