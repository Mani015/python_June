
# Understanding Scope
# In programming, the scope of a name defines the area of a program in which you can
# unambiguously access that name, such as variables, functions, objects, and so on.
# A name will only be visible to and accessible by the code in its scope.
# Several programming languages take advantage of scope for avoiding name collisions
# and unpredictable behaviors. Most commonly, you’ll distinguish two general scopes:
#
# Global scope: The names that you define in this scope are available to all your code.

# global variable is accessible local scope
Global_var = 100
# print('Global variable:',Global_var)

# def Outer():
#     def Inner():
#
#         print('Global variable:', Global_var)
#     Inner()
# Outer()
# Global variable: 100


# Global variable is accessing the enclosig scope
def Outer():
    def Inner():
        pass
    Inner()
    print('Global variable:', Global_var)
# Outer()
# Global variable: 100


G1 = 'Prasad'
# def F1():
#     def F2():
#         pass
#     F2()
# F1()
# print('global v:',G1)
# global v: Prasad









def F1():
    def F2():
        print('global v:', G2)
    F2()
F1()
# NameError: name 'G2' is not defined





