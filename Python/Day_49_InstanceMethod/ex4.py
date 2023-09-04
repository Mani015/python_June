
# class variable: A class variable is written inside of class and out side of the fucntion
# is called class variable.This variable declared only for class


class Fan:
    Fan_AdvanceFeauture = 'Less power consuming'  # class variable
    def __init__(self,name,model,wings,price):
        self.name = name
        self.model = model
        self.price = price
        self.wings = wings
    def View(self):
        print(
            self.name,
            self.price,
            self.wings,
            self.model
        )

F1 = Fan('Crompton','Diamond',1,2500)
# F1.View()
# Crompton 2500 1 Diamond
F2 = Fan('Orient','sharp',2,4000)
F3 = Fan('usha','cool',5,5000)
F4 = Fan('Bajaj','canryqueen',3,47000)
F5 = Fan('Hawels','sunflower',8,32000)

for i in [F1,F2,F3,F4,F5]:
    print('Fan_Name:',i.name)
    print('Fan_Model:',i.model)
    print('Fan_Wings:',i.wings)
    print('Fan_cost:',i.price)
    print('Fan_advantage:',i.Fan_AdvanceFeauture)
    print()

# Fan_Name: Crompton
# Fan_Model: Diamond
# Fan_Wings: 1
# Fan_cost: 2500
# Fan_advantage: Less power consuming
#
# Fan_Name: Orient
# Fan_Model: sharp
# Fan_Wings: 2
# Fan_cost: 4000
# Fan_advantage: Less power consuming
#
# Fan_Name: usha
# Fan_Model: cool
# Fan_Wings: 5
# Fan_cost: 5000
# Fan_advantage: Less power consuming
#
# Fan_Name: Bajaj
# Fan_Model: canryqueen
# Fan_Wings: 3
# Fan_cost: 47000
# Fan_advantage: Less power consuming
#
# Fan_Name: Hawels
# Fan_Model: sunflower
# Fan_Wings: 8
# Fan_cost: 32000
# Fan_advantage: Less power consuming

