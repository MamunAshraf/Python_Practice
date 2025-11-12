"""
Types of Python Inheritance
Single Inheritance: A child class inherits from one parent class.
Multiple Inheritance: A child class inherits from more than one parent class.
Multilevel Inheritance: A class is derived from a class which is also derived from another class.
Hierarchical Inheritance: Multiple classes inherit from a single parent class.


"""

#single inhetitance

class Person:
    def __init__(self,name):
        self.name=name

class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary=salary
    def show(self, name,salary):
        print(name,salary)

#single inheritance output:
e=Employee("Mamun",60000)
print(e.name,e.salary)
e.show("Mamun",50000)



#Multiple inheritance
class Job:
    def __init__(self,salary):
        self.salary=salary

class EmployeePersonJob(Employee,Job): #inherit from job and employee class
    def __init__(self, name, salary):
        super().__init__(name, salary)
        Employee.__init__(self, name, salary)  # Initialize Employee
        Job.__init__(self, salary)     #initialize Job

#output of Multiple inheritance
e2=EmployeePersonJob("Ashraf",40000)
print(e2.name,e2.salary)
e2.show("Ashraf",40000)




#multilevel inheritance

class Manager(EmployeePersonJob):
    def __init__(self, name, salary,department):
        self.department=department
        EmployeePersonJob.__init__(self,name,salary)
    def show(self,name,salary,department):
        print(name,salary,department)

#output of Multilevel inheritance

e3=Manager("Uddin",30000,"IT")
print(e3.name,e3.salary,e3.department)
e3.show("Uddin",30000,"IT")




# 4. Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, team_size):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.team_size = team_size


#output heirarchical inheritance
e4=AssistantManager("Nusrat",10000,10)      
print(e4.name,e4.salary,e4.team_size)