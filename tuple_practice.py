thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#One item tuple, remember the comma: without comma it will consider as string not tuple 

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple items can be of any data type: 
#can be string, int and anything within one tuple also 


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#indexing 

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#print 1st three items
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[0:3])

#print 2 to at the end 
print(thistuple[2:])

#This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Check if "apple" is present in the tuple:

if "apple" in thistuple:
     print("Present in this tuple")
else:
    print("Not present")


#update tuple can't update tuple. if we need to update tuple , first we need to convert it to list 

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
newtuple=list(thistuple)

print(newtuple)
newtuple[0]="kiwi"
print(newtuple)

#append in tuple 
# can't append in tuple, if we want to append ,first we need to convert it to list

thistuple = ("apple", "banana", "cherry")
newtuple=list(thistuple)
print(newtuple)
newtuple.append("orange")
print(newtuple)


#Remove Items
# can't remove in tuple, if we want to remove ,first we need to convert it to list
thistuple = ("apple", "banana", "cherry")
newtuple=list(thistuple)
newtuple.remove("apple")
print(newtuple)


#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #NameError: name 'thistuple' is not defined

#unpacking 

fruits = ("apple", "banana", "cherry")
(x,y,z) = fruits #x,y,z variable declaration and apple, banana, cherry are values 

print(x)
print(y)
print(z)

print("}-------------------------")
#we can also use Asterisk* for unpacking that means if we have much values than variable declaration 
fruits=("apple","banana","cherry","Kiwi","orange","watermelon")
(x,y,*z)=fruits
print(x)
print(y)
print(z)


print("}-------------------------")
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


#for loop in tuple

thistuple = ("apple", "banana", "cherry")
for i in thistuple:
    print(i)

#by using range

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])


#by using while 
print("----by using While loop----")
thistuple=("apple", "banana", "cherry")
i=0
while i<len(thistuple):
    print(thistuple[i])
    i=i+1


#joining tuple 

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply Tuples
tuple1=("a","b","c","d")
tuple2=2*tuple1
print(tuple2)

       
    