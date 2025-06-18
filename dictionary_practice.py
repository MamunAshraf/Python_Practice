
person={
    "f_name":"Ashraf",
    "l_name":"Mamun",
    "year": 1994
}
x=person.values()
print(x)

#Change Values
person["l_name"]="Uddin"
print(x)

y=person.items()
print(y)


#Update Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"brand": "Tayota"})
thisdict.update({"year": 2020})
print(thisdict)


#adding a key and value in a dictionary

thisdict={
    "brand":"Toyota",
    "Model":"Mustang",
    "year":1997
}

thisdict["Owner"]="Ashraf"
print(thisdict)

#The pop() method removes the item with the specified key name
thisdict.pop("year")
print(thisdict)

#The popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
del thisdict["Model"]
print(thisdict)


#Print all key names in the dictionary, one by one:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for i in thisdict:
    print(i)

#print all values

for i in thisdict:
    print(thisdict[i])

#also we can use values()

for i in thisdict.values():
    print(i)


#Loop through both keys and values, by using the items() method:

for i in thisdict.items():
    print(i)

#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict=thisdict.copy()
print(mydict)

#Make a copy of a dictionary with the dict() function:
mydict2=dict(thisdict)
print(mydict2)


#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily= {

    "child1": child1,
    "child2":child2,
    "child3":child3
}

#To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
print(myfamily["child3"]["year"])

