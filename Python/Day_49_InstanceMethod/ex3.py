# delete the instance variable
# syn: del  self.instancevariable
class Technology(object):

    def __init__(priya, Name, Price, Duration):
        priya.name = Name  # Instance variable1
        priya.price = Price  # Instance variable2
        priya.time = Duration  # Instance variable3
    def Display(priya):
        print(
            'Technology_Name:',priya.name,
            'Technology_price:',priya.price,
            "Technology_Duration:",priya.time
        )
    def deletevariable(self):
        del self.name

Course1 = Technology("pythonFullstack",25000,str(4)+'Months')
Course1.Display()
# Technology_Name: pythonFullstack Technology_price: 25000 Technology_Duration: 4Months

Course1.deletevariable()
Course1.Display()

#     'Technology_Name:',priya.name,
# AttributeError: 'Technology' object has no attribute 'name'
