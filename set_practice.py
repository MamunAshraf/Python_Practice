
myset = {"apple", "banana", "cherry"}
print(myset)


#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#false and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, 0, 2}
print(thisset)


#access set Access Items

myset = {"apple", "banana", "cherry"}
for i in myset:
    print(i)

#Check if "banana" is present in the set:
myset = {"apple", "banana", "cherry"}
if "banana" in myset:
    print("Present in set")
else:
    print("Not present")

#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Add elements from secondset into thisset:
thisset = {"apple", "banana", "cherry"}
secondset={"Kiwi","Orange"}
thisset.update(secondset)
print(thisset)

#remove Remove set Item

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)


#using pop
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)


#loop items

thisset = {"apple", "banana", "cherry"}
for i in thisset:
    print(i)


#check apple in thisset
thisset = {"apple", "banana", "cherry"}
if "apple" in thisset:
    print("Present")
else:
    print("Not Present")
