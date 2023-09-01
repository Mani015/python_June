
# Python is an object-oriented programming language.
# This means that almost all the code is implemented using a special construct called classes.
# A class is a code template for creating objects.


# What is a Class and Objects in Python?
#
# [Class: The class is a user-defined data structure that binds the data members and methods into a single unit.
# Class is a blueprint or code template for object creation. Using a class, you can create as many objects as you want.]


# Object: An object is an instance of a class.
# It is a collection of attributes (variables) and methods.
# We use the object of a class to perform actions.

# How to create a Function....?

# def Functionname():   Function creation
#     body of fucntion
#
# Functionname()  fucntion calling


# How to create class .....?
# A class created by class is a keyword

# class Classname(object):
    # body of class

# Classname()   Calling class


# Name_pascal:
# "PascalCase" is less commonly used in Python,
# but it typically involves capitalizing the first letter of each word without spaces or underscores.
# This style is often seen in class names and sometimes in module names.
# For instance: MyClass or MyModule.


# Objects have two characteristics: They have states and behaviors (object has attributes and methods attached to it) Attributes represent its state,
# and methods represent its behavior. Using its methods, we can modify its state.
#
# In short, Every object has the following property.
#
# Identity: Every object must be uniquely identified.
# State: An object has an attribute that represents a state of an object, and it also reflects the property of an object.
# Behavior: An object has methods that represent its behavior.
#
# A real-life example of class and objects.
#
# Class: Person
#
# State: Name, Gender, Profession
#
# Behavior: Working, Study
#
# Using the above class, we can create multiple objects that depict different states and behavior.
#
# Object 1: Jessa
#
# State:
# Name: Jessa
# Gender: Female
# Profession: Software Engineer
#
# Behavior:
# Working: She is working as a software developer at ABC Company
# Study: She studies 2 hours a day
#
# Object 2: Jon
#
# State:
# Name: Jon
# Sex: Male
# Profession: Doctor
#
# Behavior:
# Working: He is working as a doctor
# Study: He studies 5 hours a day


# Class Creation
class Person:
    Person_name = 'Jhansi' # class Variable1
    Person_age = 21 # class Variable2
    Person_Addres = 'Annavaram' # class Variable3

# class calling by using object:
# object creation  sysntax: New_objectname = ClassName()
Man1 = Person()  # object1
Man2 = Person() # object2
Man3 = Person()# object3


