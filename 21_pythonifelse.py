#python Condition and If Statement 
## Example of IF Statement 
a=33
b=200
if b>a:
    print("B is greater than A")

##the Elif Keyword in the Python way to Saying that if the previous Conditon is not True please print Condition
a=33
b=200
if b<a:
    print("B is greater than A")
elif a>b:
    print("b is greater than a")
## else catch any thing 
a=33
b=200
if b<a:
    print("B is greater than A")
elif a>b:
    print("b is greater than a")
else:
    print("a is not equal to b")    
##Short hand if 
a=33
b=200
if a>b:print("a is greater than b") 
## Short hand if -----else
a=33
b=200
print("yes is greater than b") if a>b else print ("no it is not greater")

# One line if else statement with 3 Condition 
a=33
b=33
print("A") if a>b else print("=") if a==b else print("B")

# And is the logical operation and it is used to combine the condition Statement 

a=200
b=20
c=500
if a>b and b<c:
    print("both the Condition are true")

## or is the logical operation and it is used to combine the logical statement 
a=200
b=20
c=500
if a>b or b>c:
    print("Any one Codition is true")
## nested if Statement if you have if statement inside the if statement (** very very important )
x=41
if x>10:
    print("if is above 10")
    if x>20:
        print("and it is also above 20")
    else:
        print("but it is both above 20")    

## the Pass Statement if with any reason if Statement has no content than you can pass thestatement for Avoing the error in program 
a=33
b=200
if b>a:
    pass
