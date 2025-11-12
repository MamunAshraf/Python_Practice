#poly-->many
#morphism-->form

#1.Method overriding 

#parents er kono method/function jodi child class e over ride kore take boli methodoverriding bole
class Grandfather:
    def greet(self):
        print("Grandfather says Hello")
class Father(Grandfather):
    def greet(self):
        print("Father says Hello")

class Child(Father):
    def greet(self):
        print("Child says Hello")

gf=Grandfather()
f=Father()
c=Child()

gf.greet()
f.greet()
c.greet()


#method overloading 


