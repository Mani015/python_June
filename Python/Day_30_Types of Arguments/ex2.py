
def Student(name,age,location):
    print('Student_Name:',name)
    print('Student_age:',age)
    print('Student_location:',location)
# Student('Sravani',20,'Chennai')
# Student_Name: Sravani
# Student_age: 20
# Student_location: Chennai
print()
# Student('Padma_Priya',21)
# TypeError: Student() missing 1 required positional argument: 'location'


def Number(x,y,z):
    print('x is :',x)
    print('y is :',y)
    print('z is :',z)
# Number(1,2,3)
# x is : 1
# y is : 2
# z is : 3

x = 12
z = 23
y = 15
Number(z,x,y)

# x is : 23
# y is : 12
# z is : 15