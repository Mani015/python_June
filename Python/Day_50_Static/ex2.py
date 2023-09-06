
# To update class variable value by using classmethod

class Laptop(object):
    caution1 = 'Your laptop charging below 10%, please insert your charger'
    caution2 = 'please update your laptop daily'
    def __init__(self,lname,lprice):
        self.name = lname
        self.price = lprice
        print(self.caution1)  #Your laptop charging below 10%, please insert your charger

    #update the class variable value
    @classmethod
    def Update_caution1(cls,Newcaution):
        cls.caution1 = Newcaution
        print(cls.caution1)

lt1 = Laptop('Dell',50000)
lt1.Update_caution1('Your laptop charging below 15%, please insert your charger')
# Your laptop charging below 15%, please insert your charger
