## Print Each item of variable in Loop
fruits=["Apple","Bananna","Cherry"]
for i in fruits:
    print(i)

##loop through String 

for i in "banana":
    print(i)

## the Break Statement 
fruits=["Apple","Banana","Cherry"]
for i in fruits:
    print(i)
    if i == "Banana":
        break
## Exit the Loop when i is "Banana" but this time the brake comes before print
for i in fruits:
    
    if i == "Banana":
        break  
    print(i)
#the Continue Statement 
for i in fruits:
    
    if i == "Banana":
        continue  
    print(i)   
##the Range() Function
for i in range(6):
    print(i)    

##Example of Some deep Range
for i in range(2,6):
    print(i)    
## you can Specify value of Increment by Ading the 3rd parameter 
for i in range(2,30,4):
    print(i)    

##Else in For loop
for i in range(6):
    print(i)
else:
    print("You Are garbadge Bhosdike")    

##now We can brank the loop in 3 and the else willbe the garbadge 
for i in range(6):
    if i==3:
        break
    print(i)
else:
    print("Why you are garbdge")    

## Nested loop 
adj=["Red","big","testy"]
fruits=["Apple","Bananna","Cherry"]  

for i in adj:
    for j in fruits:
        print(j,i)
## the pass Statement 

for i in [0,1,2]:
    pass