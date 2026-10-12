class employee:
    def __init__(self,eid,en,edesig):
        self.e_id =eid
        self.ename =en
        self.edesignate =edesig
    def display(self):
        print("Employee Id:",self.e_id)
        print("Employee name:",self.ename)
        print("Employee designation:",self.edesignate)
    def getemp(self):
        self.e_id =input("Enter the emp_id:")
        self.ename =input("Enter the emp_name:")
        self.edesignate =input("Enter the emp_designation:")
a1=employee("emp1","Agila","manager")
a1.display()
a2=employee(None,None,None)
a2.getemp()
a2.display()