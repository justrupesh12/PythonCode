# Python is an Object orianted programming language
## Almost everything in python is object Its property and method
## A "CLASS" is like object Contructor or a blue print of an object

## Create and class
class myclass:
    x=5
print(myclass)    ## output:- <class '__main__.myclass'>

## Create Object
class myclass:
    x=5
p1=myclass()
print(p1.x)## output 5

## the __init __() Function

class person:
    def __init__(self,name ,age):
        self.name=name
        self.age=age
p1=person("Rupesh",27)
print(p1.name)## Rupesh
print(p1.age)   ## 27     

## object method 

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunction(self):
        print("hello everyone my name is " +self.name)  
p1=person("Rupesh",27)   
p1.myfunction()     

##  the self Parameter 
class person:
    def __init__(rupeshobject,name,age):
        rupeshobject.name=name
        rupeshobject.age=age
    def myfunction(abc):
        print("hello everyone my name is " +abc.name)  
p1=person("Rohit",27)   
p1.myfunction()  

## How to Modify object properties
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunction(self):
        print("hello everyone my name is " +self.name)  
p1=person("Rupesh",27)   
p1.age=25  
print(p1.age)

##Delete object properties
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunction(self):
        print("hello everyone my name is " +self.name)  
p1=person("Ravi",27)   
del p1.age
print(p1.name)

##pass statement
class person:
    pass