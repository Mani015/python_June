# Let’s see how to create a factory method using the class method.
# In this example, we will create a Student class object using the class method.

from datetime import date
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

x1 = Student('Jessa', 20)
# x1.show()
# Jessa's age is: 20



# create new object using the factory method
joy = Student.calculate_age("Jhansi", 1997)
joy.show()
# Jhansi's age is: 26

Roy = Student.calculate_age('Anusha',2002)
Roy.show()
# Anusha's age is: 21
