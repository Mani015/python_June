
# Protected variables:
# 1).protected variable,2).Method
# It is denoted by the single underscore ' _ '

class Student:
    def __init__(self,name,age,rollno,location):
        self._name = name  # protected variable_1
        self._age = age  # protected variable_2
        self._rollno = rollno # protected variable_3
        self._location = location # protected variable_4
    def Appear(self):
        print(
            self._name,self._age,self._rollno,self._location
        )

ob1 = Student('Anusha',20,123,'vijayawada')
ob1.Appear()
# Anusha 20 123 vijayawada