class Parent:
    def __init__(self,ename,eage,egender,eid,esalary,edomain):
        self.name = ename
        self.age = eage
        self.gender = egender
        self.id = eid
        self.salary = esalary
        self.domain = edomain
class Frsher_level(Parent):
    def __init__(self,ename,eage,egender,eid,esalary,edomain,efresher):
        Parent.__init__(self,ename,eage,egender,eid,esalary,edomain)
        self.fresher = efresher

    def View(self):
        print(
            self.name, self.age, self.gender, self.id, self.salary, self.domain, self.fresher
        )
class Experience_level(Parent):
    def __init__(self,ename,eage,egender,eid,esalary,edomain,eexp,estatus):
        Parent.__init__(self, ename, eage, egender, eid, esalary, edomain)
        self.exp = eexp
        self.status = estatus
    def View(self):
        print(
            self.name, self.age, self.gender, self.id, self.salary, self.domain, self.exp,self.status
        )
ob1 = Frsher_level('Prasad',21,'male',101,50000,'PFS','fresher')
ob1.View()
ob2 = Experience_level('padmapriya',21,'female',105,60000,'Devops','3+years','unmaaried')
ob2.View()

# padmapriya 21 female 105 60000 Devops 3+years unmaaried