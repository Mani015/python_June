
class Technology(object):

    def __init__(priya, Name, Price, Duration):
        priya.name = Name  # Instance variable1
        priya.price = Price  # Instance variable1
        priya.time = Duration  # Instance variable1
    def Display(priya):
        print(
            'Technology_Name:',priya.name,
            'Technology_price:',priya.price,
            "Technology_Duration:",priya.time
        )
    def Update_Coursename(priya, New_course):
        priya.name = New_course
    # update the course fees:
    def Increment_Fees(priya,Additional_fees):
        priya.price+=Additional_fees
    def Decrement_Fees(priya,subraction_fees):  # Decrement by using instance method
        priya.price-=subraction_fees


Course1 = Technology("pythonFullstack",25000,str(4)+'Months')
Course1.Display()
# Technology_Name: pythonFullstack Technology_price: 25000 Technology_Duration: 4Months
print()
Course1.Increment_Fees(5000)
Course1.Display()


# Technology_Name: pythonFullstack Technology_price: 30000 Technology_Duration: 4Months

Course1.Decrement_Fees(7500)
Course1.Display()

# Technology_Name: pythonFullstack Technology_price: 22500 Technology_Duration: 4Months
