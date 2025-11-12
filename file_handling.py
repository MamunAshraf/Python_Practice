#read a txt file

file=open('name.txt', 'r')
content=file.read()
print(content)

file.close()

#another way to open a file

with open('name.txt','r')as f:
    content=f.read()
    print(content)

#write in a file 

#by using 'w', in  text file previous lines will be removed and new line wil write in txt file.
with open('name.txt','w') as f:   
    f.write("Hello world\n")
    f.write("I a writing in a file\n")

#we want both , previous text mesg also 

with open('name.txt', 'a') as f:
    f.write("Hi This is Ashraf\n")
    f.write("I am from Chittagong\n")

#write list in file 

list=['\nI love python','\nI am new at python','\nI need to get admin at ostad']
with open('name.txt','a')as f:
    f.writelines(list)


#exception handling 


try:
    with open('Mamun.txt', 'r')as f:
        print(f.read())
    print(10/0)
    x=int('abc')
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Zero division is not possible")
except ValueError:
    print('invalid value')


#try with zero division error



