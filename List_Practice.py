#Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Items is found")
else:
    print("Items is not found")

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3]=["Kiwi"]
print(thislist)

#Insert "watermelon" as the third item:
#insert has two agrument

thislist.insert(2,"watermelon")
print(thislist)

#Using the append() method to append an item:
thislist.append("Orange")
print(thislist)


#Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
thislist1 = ["mango", "pineapple", "papaya"]
thislist.extend(thislist1)
print(thislist)


#tuple
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)

#If there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry", "apple","apple"]
thislist.remove("apple")
print(thislist)

#The pop() method removes the specified index.
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[1]
del thislist[0]
print(thislist)

#The clear() method empties the list.
thislist.clear()
print(thislist)


#You can loop through the list items by using a for loop:  
thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i)

#Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


print("Print all items, using a while loop to go through all the index numbers")
thislist = ["apple", "banana", "cherry"]
i=0
while i<len(thislist):
    print(thislist[i])
    i+=1

#A short hand for loop that will print all items in a list:
print("---------------------------")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]





fruits=["apple","banana","cherry","Kiwi","chocolate"]
list1=[]
for i in fruits:
   if "c" in i:
      list1.append(i)
print(list1)

fruits=["apple","banana","cherry","Kiwi","chocolate"]
newlist2=[i for i in fruits if "c" in i]
print(newlist2)

#Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist2=[2,1,3,5,4,2]
thislist2.sort()
print(thislist2)

#Sort Descending
thislist2.sort(reverse=True)
print(thislist2)

thislist2.sort(reverse=False)
print(thislist2)

#Sort the list based on how close the number is to 50:

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
mylist1=thislist.copy()
print(mylist)
print(mylist1)

#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#by using for loop

for i in list2:
   list1.append(i)
print(list1)

#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c","d"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
print(newlist)


