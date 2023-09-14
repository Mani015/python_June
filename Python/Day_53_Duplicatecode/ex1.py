# emp1 = name,age,gender,id,salary,domain,fresher
# emp2 = name,age,gender,id,salary,domain,experience,status
class Employee:
    def __init__(self,ename,eage,egender,eid,esalary,edomain,efresher):
        self.name = ename
        self.age = eage
        self.gender = egender
        self.id = eid
        self.salary = esalary
        self.domain = edomain
        self.fresher = efresher
    def View(self):
        print(
            self.name,self.age,self.gender,self.id,self.salary,self.domain,self.fresher
        )
ob1 = Employee('Prasad',21,'male',101,50000,'PFS','fresher')
# ob1.View()
# Prasad 21 male 101 50000 PFS fresher

ob2 = Employee('Girish',23,'male',103,70000,'JFS','2years','married')
ob2.View()

# ob2 = Employee('Girish',23,'male',103,70000,'JFS','2years','married')
# TypeError: __init__() takes 8 positional arguments but 9 were given