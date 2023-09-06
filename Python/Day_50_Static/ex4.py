
# Define Static Method in Python
# Any method we create in a class will automatically be created as an instance method.
# We must explicitly tell Python that it is a static method using the @staticmethod decorator or staticmethod() function.
#
# Static methods are defined inside a class, and it is pretty similar to defining a regular function.
# To declare a static method, use this idiom:

# Python program to
# demonstrate static methods

class Person:
    def __init__(self, name):
        self.name = name
        # self.age = age

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        if age>18:
            return 'This candiate above 18 years'
        else:
            return 'This candiate below 18 years'

x1 = Person('anusha')
print(x1.isAdult(21))
# This candiate above 18 years



