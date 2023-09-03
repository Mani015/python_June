
# How to get the class variables.. by using object name
# syn: class_Name.Class_variable

class Car:
    carname = 'Mahindra THOR'
    carcolor = 'Black'
    cartype = 'Mannual'
    carengine = 'dual engine'
    carfuel = 'EV'
    carprice = 1800000
    print(carname)
    print(carcolor)
    print(cartype)
    print(carprice)
    print(carfuel)
    print(carengine)

# Creating object for class
# New_objectname = class_Name()

Obj1 = Car()
# print(Obj1)
# Mahindra THOR
# Black
# Mannual
# 1800000
# EV
# dual engine
# <__main__.Car object at 0x00000253F91B1F40>


# class variable calling by objectname
# syn : object_name.class variable_name
print()
print('Object calling')
print(Obj1.carname,Obj1.carfuel,Obj1.cartype,Obj1.carprice,Obj1.carengine)

# Object calling
# Mahindra THOR EV Mannual 1800000 dual engine
