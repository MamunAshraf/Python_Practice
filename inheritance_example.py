#single inheritance
class Grandfather:
    def __init__(self,color,l_name):
        self.color=color
        self.l_name=l_name
    def gf_method(self):
        print("I am from Grandfather Method")

class Father(Grandfather):
    def __init__(self,hobby,color,l_name):
        super().__init__(color,l_name)  #inherit from super cls from Grandfather
        self.hobby=hobby
    def fat_method(self):
        print("I am from father Method")
#multi level inheritance.

class Child(Father,Grandfather):  
    def __init__(self, fashion,hobby, color,l_name):
        super().__init__(hobby, color, l_name)
        self.fashion=fashion
    def child_method(self):
        print("I am from Child Method")


gf1=Grandfather("red","Chowdhury")
f1=Father("Cricket","red","Chowdhury")
print(f1.l_name)
print(f1.color)


c1=Child("Hip Hop", "Badminton","Blue","Chowdhury")
print(c1.fashion,c1.hobby,c1.color,c1.l_name)


#c1.child_method()
#c1.fat_method()
#c1.gf_method()

##nultiple inheritance example 
print("--------------------------")
print("--------------------------")
print("--------------------------")


class Class1:
    def __init__(self,color,l_name):
        self.color=color
        self.l_name=l_name

class Class2:
    def __init__(self,hobby):
        self.hobby=hobby

class Class3(Class2,Class1):
    def __init__(self,fashion):
        self.fashion=fashion
        Class2.__init__(self,hobby)
        Class1.__init__(self,color,l_name)

c=Class3("Hip Hop","Red","Chow")



