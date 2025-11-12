#hairarchical example

class vehical:
    def engine_type(self):
        print("vechicle has an engine")

class car(vehical):
    def num_doors(self):
        print("car has four door")
class Truck(vehical):
    def load_capacity(self):
        print("Truck can caryy 10 tons")

c1=car()
c1.engine_type()

t=Truck()
t.load_capacity()


#Hybrid Inheritance 

class Shape:
    def Area(self):
        print("Area is calculating")
class Polygon(Shape):
    def sides(self):
        print("Polygon has multiple sides")
class Rectangle(Polygon):
    def __init__(self, length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    
rec=Rectangle(10,3)
print(rec.area())
rec.sides()
rec.Area()
