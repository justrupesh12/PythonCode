#Casting And calling a function

def my_function():
    print("This is a Rupesh Kumar")
my_function()

#Defination of Arguments:- if you have Any information written under function is called Arguments
## generally arguments is given After Function name and inside the Paranthasis

def my_function(fname):
    print(fname +"Khare")
my_function("Sharad")   
my_function("sanjay") 
my_function("dilip")  

#Number of agruments 2 args
def my_function(fname,lname):
    print(fname +" "+lname)

## Arbitiary Argument *args

def my_Functiom(*kids):
    print("The Youngest Child name is " +kids[2])
my_Functiom("Chintu","Ram","Rohan")

## Keyword Argument key value

def my_function(Child1,Child2,Child3):
    print("the youngest child is "+Child3)
my_function(Child1="RAM",Child2="Laxman",Child3="Sita")   

##*** Arbitary Keyword Argument (** Double Star is used in this Arbiratery)

def my_function(**kids):
    print("His  last name is " + kids["lname"])
my_function(fname="sharad",lname="Khare")   

## Passing a List as a Aggument 
def my_function(food):
    for i in food:
        print(i)
Fruits=["orange","Papaya","banana"]
my_function(Fruits)    

##Return Value:- to list a function return a value than you use returen value
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(8))

## Pass Statement 


def my_fun(x):
    pass 