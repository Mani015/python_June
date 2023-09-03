class fan(object):
    def __init__(self,fan_name,fan_clor,fan_model,fan_price):
        self.fname=fan_name
        self.fcolor=fan_clor
        self.fmodel=fan_model
        self.fprice=fan_price
    def display(self):   #instants method
        print( self.fname,self.fcolor, self.fmodel,self.fprice)
# with object
obj1=fan('ganga','white','three wings',4000)

obj1.display()     #using obj1 to calling method
obj2=fan("cromptom","black",str(1)+"wings",5000)
obj2.display()     #using obj2 to calling method

