
# def __init__(self):
#     # body of the constructor
# Where,
#
# def: The keyword is used to define function.
# __init__() Method: It is a reserved method. This method gets called as soon as an object of a class is instantiated.
# self: The first argument self refers to the current object.
# It binds the instance to the __init__() method.
# It’s usually named self to follow the naming convention.


class Mobile(object):
    def __init__(self,Mobile_Name,Mobile_Color,Mobile_Price,Mobile_RAM,Mobile_ROM):
        # object.variablename = parameter1
        self.Mname = Mobile_Name  # Instance variable1
        self.Mcolor = Mobile_Color # Instance variable2
        self.Mprice = Mobile_Price # Instance variable3
        self.MRam = Mobile_RAM # Instance variable4
        self.Mrom = Mobile_ROM # Instance variable5
        print(
            self.Mname,self.Mcolor,self.Mprice,self.MRam,self.Mrom
        )


# Without creating object:

Mobile('vivo','Green',14000,str(3)+'GB',64)
# vivo Green 14000 3GB 64
Mobile('samsung','gold',20000,str(6)+'GB',128)
# samsung gold 20000 6GB 128



