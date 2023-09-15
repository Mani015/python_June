# In other words, when a subclass defines a method with the same name, parameters, and return type as a method in its parent class,
# it is said to be overriding the method from the parent class.
#
# Method overriding allows you to provide a specialized implementation of a method in the subclass
# while maintaining the same method signature as in the superclass.
# This is useful for customizing the behavior of a method in a subclass to suit
# its specific needs while still inheriting and reusing code from the superclass.
class Human:
    def __init__(self,Name,Age,gender,height,weight):
        self.name = Name
        self.age = Age
        self.gender = gender
        self.height = height
        self.weight = weight
    def Appear(self):
        print(self.name,self.age,self.gender,self.height,self.weight)

class Person1(Human):
    def __init__(self, Name, Age, gender, height, weight,address,number):
        self.name = Name
        self.age = Age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.addres = address
        self.number = number

# ob1 = Person1('Padma_Priya',10,'Female',str(5)+'feet',25)


# TypeError: __init__() missing 2 required positional arguments: 'address' and 'number'



x = 10
x = 20
print(x)
# 20