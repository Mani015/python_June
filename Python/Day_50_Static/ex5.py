
def Main_Function(name):
    class Who(object):
        def __init__(self,age):
            self.age = age
            # print(self.age)
        def View(self):
            print('my age is :',self.age)
            print('My name is:',name)
    return Who

ob1 = Main_Function('sitha')
ob2 = ob1(21)
ob2.View()

# my age is : 21
# My name is: sitha























