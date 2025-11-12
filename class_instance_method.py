class Democlass:
    def instance_method(self):
        print("This is a instance method")
    
    @classmethod
    def class_method(cls):
        print("This is a class method")

    @staticmethod
    def static_method():
        print("this is a static method")


d1=Democlass()
d1.instance_method()
d1.static_method()
d1.class_method()
