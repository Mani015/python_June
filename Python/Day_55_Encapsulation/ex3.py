# pop: variable, operator,loops , fucntions(procedural oriented programming) -->NO data secure

# oop: class, object, Inheritance,polymorphism,abstraction-----> Data secure

# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP)
#  It describes the idea of wrapping data and the methods that work on data within one unit.

# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.


# There are multiple methods that are offered by Python to limit variable and method access across the program. Let’s go over the methods in detail.
# There are 3 access modifier
# public Access Modifier
# Protected Access Modifier
# Private Access Modifier


# public Access Modifier
# With out inheritance
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def Display(self):
        print(
            self.name,self.age,self.salary
        )
ob1 = Employee('Sravani',22,50000)
ob1.Display()
# Sravani 22 50000
