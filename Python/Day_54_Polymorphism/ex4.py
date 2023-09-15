# method overloading:
# single class, multiple methods with same name , and different parameters.


# # Method overloading in Python refers to the ability to define multiple methods with the same name in a class,
# # but with different parameter lists. This allows a class to have multiple methods with the same name,
# # but each method can take a different number or types of arguments.
# # When a method is called, Python determines which version of the method to invoke based on the number and types
# # of arguments provided during the function call.
class Addition:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        print(self.a,self.b,self.c)
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(self.a, self.b)
    def __init__(self,a):
        self.a = a
        print(self.a)
    def __init__(self):
        print('THis is mehtod overloading')

# Addition(10)
# 10

# Addition(10,20)
# TypeError: __init__() takes 2 positional arguments but 3 were given

Addition()
# TypeError: __init__() takes 1 positional argument but 2 were given