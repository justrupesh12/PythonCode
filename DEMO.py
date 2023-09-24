print("\"this is pappu bacha . Become a Don of this year \"")

x=str(6.7)
print(type(x))

print("\"Hello, I'm \'Rupesh\', it's nice to meet you!\"")

#12 star print 
#total space (1,2,3)
print("*****\n *** \n  *")

# name =input("Please Enter your Name ")
# print("Your name is " +name+".")
# print(type(name))


# Globle Variable :- the variable which Create outside the Function.
x= "Awesome"

def myFunction():
    print("You Are "+ x)
myFunction()
print("Python is "+ x)
#Example of Globle variable 
x= "Dil mange more "
def myfunc():
    global x
    x="Fantastic"
myfunc()
print("Python is "+ x)    

# # How to get the the Integer Vale in input 
# user_int=int(input("Please Enter the value:-"))
# print(user_int)
# print(type(user_int))

#Function Example With one parameter 

def function_name(Parameter):
    print(Parameter+2)

function_name(9)    

#Function Example With multiple parameter
first_str="The Number "


def func_name(p1,p2,p3):
    print(p1+ str(p2)+p3)

func_name(first_str,5," an integer")   

#Another example with Return
def default_name(num1=7,num2=8):
    return num1 * num2
#Range Testing
x= range(1,10)
for i in x:
  print(i)

name1 =["Pappu","Gulabo","Dharo"]
name2 =["Ram","Rohit","Pappu"]
name3=name1.symmetric_difference(name2)
print(name3)






