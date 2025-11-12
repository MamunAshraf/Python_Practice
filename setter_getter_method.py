class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary  #by convention it is private variable but logically it's not

    def get_salary(self, password):
        if(password=="admin"):
            print(f"{self.name}'s salary is {self._salary}")
        else:
            print("Invalid Access!!!")
    
    def set_salary(self,password,salary):
        if(password=="admin"):
            self._salary=salary
            print(f"New salary: {self._salary}")
        else:
            print("invalid Access!!!")


e1=Employee("Karim",20000)
e1.get_salary("admin")

e2=Employee("Rahim",50000)
e2.set_salary("admin",50000)

e3=Employee("Jamal",70000)
e3.get_salary("admin")