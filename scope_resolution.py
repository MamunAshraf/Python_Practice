#scope --> region where a variable can be accessed 
#global variable 

#LEGB--> Local, Enclosing, Global, Built in 

x=10

def function(x,y):
    result=x+y
    print(result)
    print(x)
function(2,3)

print(x)


#here n is global variable 
n='global'

def outer():
    n='enclosing'
    def inner():
        #global n # update global variable 
        nonlocal n # we can update enclosing variables by using nonlocal key words
        n='local'
        print(n)
    inner()
    print(n)
outer()
print(n)


