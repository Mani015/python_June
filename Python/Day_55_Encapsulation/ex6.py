
class Student:
    def __init__(self,name,age,rollno,location):
        self._name = name  # protected variable_1
        self._age = age  # protected variable_2
        self._rollno = rollno # protected variable_3
        self._location = location # protected variable_4
    def _Appear(self):
        print(
            self._name,self._age,self._rollno,self._location
        )
class Student1(Student):
    def _New(self):
        print(
            self._name, self._age, self._rollno, self._location
        )
ob1 = Student1('padma priya',19,234,'Kadapa')
ob1._New()
# padma priya 19 234 Kadapa

print(ob1._rollno)
# 234

