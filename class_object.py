#create a class Car and two objects of it. 
#1. default constructor

class Car:
    def __init__(self):
        self.brand=""
        self.model=""

car1 =Car()
car1.brand="Toyota"
car1.model="corolla"

print(car1.brand,car1.model)

car2=Car()
car2.brand="Honda"
car2.model="Civic"
print(car2.model,car2.brand)


#create a class Student who has 2/3 attributes and create 2 objects by default constructor


class Students:
    def __init__(self):
        self.f_name=""
        self.l_name=""
        self.Marks=""

s1=Students()
s1.f_name="Mamun"
s1.l_name=" Ashraf"
s1.Marks="90"

print(s1.f_name, s1.l_name,s1.Marks)


s2=Students()
s2.f_name="Mahir"
s2.l_name="Shadman"
s2.Marks="100"

print(s2.f_name,s2.l_name,s2.Marks)

#2. parameterized constructor create a class of students and one object , value must be passed as parameter. 

class Student:
    def __init__(self,f_name,l_name,marks):
        self.f_name=f_name
        self.l_name=l_name
        self.marks=marks

s3=Student("Shsrif","islam",90)  
print(s3.f_name,s3.l_name,s3.marks)      