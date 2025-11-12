#lambda function is anonymun function , unnamed use: short cut . ekta boro code choto korte parbo

def square(x):
    return x*x
print(square(5))

#define lambda
# lambda argument : expression 

square=lambda x : x*x
print(square(2))

#add 2 digit by using lambda 

add=lambda a,b : a+b
print(add(2,3))


#sub 2 digit using lambda
sub=lambda a,b : a-b
print(sub(3,2))

#add three variables using lambda

x=lambda a,b,c: a+b+c
print(x(1,2,3))

#sort a tuple by using lambda

students=[('Rahim',50),('Karim',20),('Ashraf',80),('Uddin',60)]
sorted_students=sorted(students,key =lambda x :x [1])
print(sorted_students)

#practice again sort a tuple by using lambda function 

x=[('a',40),('b',30),('c',10,),('d',10)]
sort_x=sorted(x, key=lambda x: x[1])
print(sort_x)

#map function. list modify
#map(ki korte chacci, kar upor korte chacci)

num=[1,2,3,4]

sq_num=list(map(lambda x: x*x, num))
print(sq_num)

#filter function 

#first find even number by using map

even= list(map(lambda x :x%2==0,num))
print(even)

#now using filter function from a list

even1=list(filter(lambda x : x%2==0,num))
print(even1)