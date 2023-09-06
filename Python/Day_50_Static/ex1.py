# class method:
# Class method: Used to access or modify the class state.
# In method implementation, if we use only class variables,
# then such type of methods we should declare as a class method.
# The class method has a cls parameter which refers to the class.




# Create Class Method Using @classmethod Decorator
# To make a method as class method, add @classmethod decorator before the method definition,
# and add cls as the first parameter to the method.


class Vehicel(object):
    Caution = 'Please go and slow'
    def __init__(self,Vname,Vprice,Vnumber,Vcolor):
        self.name = Vname
        self.price = Vprice
        self.number = Vnumber
        self.color = Vcolor
    def Display(self):
        print(
            self.name,self.price,self.number,self.color
        )
    # class variable name to get by using instance method
    def CallingClassvariable(self):
        print(self.Caution)
    @classmethod
    def Classmethod(cls):
        print(cls.Caution)


v1 = Vehicel('Volvo',1000000,'ap0404','balck')
v1.Display()
# Volvo 1000000 ap0404 balck
# v1.CallingClassvariable()
# Please go and slow

# class variable to call using classmethod
# syn: objectname.classmethod()
v1.Classmethod()
# Please go and slow

