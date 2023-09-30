
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def Display(self):
        print(
            self.name,self.age,self.salary
        )
class Emp1(Employee):
    def Show(self):
        print(self.name,
              self.age,
              self.salary)

b1  = Emp1('Jhansi',19,70000)
b1.Show()
# Jhansi 19 70000

print(b1.name)
# Jhansi
