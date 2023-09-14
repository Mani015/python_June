class Employee:
    def __init__(self,ename,eage,egender,eid,esalary,edomain,efresher,eexp,estatus):
        self.name = ename
        self.age = eage
        self.gender = egender
        self.id = eid
        self.salary = esalary
        self.domain = edomain
        self.exp = eexp
        self.status = estatus
    def View(self):
        print(
            self.name,self.age,self.gender,self.id,self.salary,self.domain,self.exp,self.status
        )
ob2 = Employee('Girish',23,'male',103,70000,'JFS','2years','married')
ob2.View()
# Girish 23 male 103 70000 JFS 2years married