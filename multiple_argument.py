x=2
y=3
print(x+y)

#argument 

def multiple_two_nums(a,b):
    return a*b
result=multiple_two_nums(2,3)
print(result)

def hello():
    return "Hello"
greetings=hello()
print(greetings)

def addition(a,b):
    result=a+b
    return result
r=addition(12,10)
print(r)

#multiple arg capture 

def add(*args):
    print(args)
    return sum(args)
r-add(1,2,3,4,5)
print(r)

#key_arguments

def my_func(f_name,l_name,age):
    print(f"My name is {f_name} {l_name}. I am {age} old person")
my_func('Mamun', 'Ashraf', 30)
#arg not defined
my_func(30,'Mamun','Ashraf')

#we can do this way
my_func(age=30,f_name='Mamun',l_name='Ashraf')

#arbitary number of key words argument
#we can use both **kwargs and **data
def my_funtion(**kwargs):
    print(kwargs)

my_funtion(age=30,f_name="Ashraf",l_name="Mamun",Marks=90)

#we can call by using kwargs


def practice(**kwargs):
    print(f"My name is {kwargs['f_name']} {kwargs['l_name']}. I am {kwargs['age']}years old person. I got {kwargs['marks']} in programming. And last I live in {kwargs['loc']}")
practice(l_name="Ashraf",f_name="Mamun", age=30,marks=90,loc="Dhaka")