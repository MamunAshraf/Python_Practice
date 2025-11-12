class Dog:
    # Class variable
    species = "Canine"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

# Creating instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing class variable
print(f"{dog1.name} is a {Dog.species}") # Output: Buddy is a Canine
print(f"{dog2.name} is a {Dog.species}") # Output: Max is a Canine

# Accessing instance variables
print(f"{dog1.name} is {dog1.age} years old") # Output: Buddy is 3 years old
print(f"{dog2.name} is {dog2.age} years old") # Output: Max is 5 years old

# Modifying class variable
Dog.species = "Domesticated Canine"
print(f"{dog1.name} is a {Dog.species}") # Output: Buddy is a Domesticated Canine
print(f"{dog2.name} is a {Dog.species}") # Output: Max is a Domesticated Canine

# Modifying instance variable
dog1.name = "Charlie"
print(f"{dog1.name} is {dog1.age} years old") # Output: Charlie is 3 years old
print(f"{dog2.name} is {dog2.age} years old") # Output: Max is 5 years old

print("----------------------------------------")
print("----------------------------------------")
print("----------------------------------------")

class Dog: 
    #class variable
    species="canine"

    def __init__(self, name,age):
        #instance variable
        self.name=name
        self.age=age

#creating instance. 

d1=Dog("Buddy",20)
d2=Dog("Max",23)
        

#accessing class varibale 
print(f"{d1.name} is a {Dog.species}")
print(f"{d2.name} is a {Dog.species}")

#accessing instance variables

print(f"{d1.name} is {d1.age} years old")
print(f"{d2.name} is a {d2.age} years old")

#modifying class variables

Dog.species="Domestic Canian"
print(f"{d1.name} is a {Dog.species}")
print(f"{d2.name} is a {Dog.species}")


#modifying instance variable 
d1.name="Charley"
d2.name="ketty"
print(f"{d1.name} is a {d1.age} years old")
print(f"{d2.name} is a {d2.age} years old")

