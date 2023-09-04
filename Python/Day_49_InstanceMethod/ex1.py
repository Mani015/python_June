# Instance method: Used to access or modify the object state.
# If we use instance variables inside a method, such methods are called instance methods.
# It must have a self parameter to refer to the current object.


class Technology(object):
    def __init__(self,Name,Price,Duration):
        self.name = Name
        self.price = Price
        self.time = Duration
    def Display(self):
        print(
            'Technology_Name:',self.name,
            'Technology_price:',self.price,
            "Technology_Duration:",self.time
        )
    def Update_Coursename(self,New_course):
        self.name = New_course

Course1 = Technology("pythonFullstack",25000,str(4)+'Months')
Course1.Display()
# Technology_Name: pythonFullstack Technology_price: 25000 Technology_Duration: 4Months
print()
Course1.Update_Coursename('JavaFullstack')
Course1.Display()

# Technology_Name: JavaFullstack Technology_price: 25000 Technology_Duration: 4Months
