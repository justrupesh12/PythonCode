x=["Apple","Banana","Orange"]
print(x)
#Duplicate Vale 
x=["Apple","Banana","Orange","Orange"]
print(x)
#list Length
x=["Apple","Banana","Orange"]
print(len(x))

#List item -Data Type.

x=["x","y","z"]
y=[1,2,3,4,5]
z=[True,False,True]

#A list With String , Int, Boolean
x=["Rupesh",45,True,"Male"]
print(x)
#Data Type For List 

x=["Rupesh",45,True,"Male"]
print(type(x))

#the List() Constructor
x=list(("Rupesh",50,True,"Male"))
print(type(x))

#Python Collection (Arrays)

#Four types of Data type in Python to learn
# 1.list 2,Tuple 3.Set ,4.Dict
#How To Access the ITeM 
x=["Apple","Banana","Orange"]
print(x[1])
x=["Apple","Banana","Orange","Mango","PineApple"]
print(x[2:5])

# Negative Indexing
x=["Apple","Banana","Orange","Cherry","Mango","PineApple"]
print(x[-6:-1])

#Leaving the Start value
x=["Apple","Banana","Orange","Cherry","Mango","PineApple"]
print(x[:4])

#How to check if item is Exist in list 

x=["Apple","Banana","Orange","Cherry","Mango","PineApple"]

if "Orange" in x:
    print("yes 'orange 'Item is Avialable") 

#Change the item value of the list
x=["Apple","Banana","Orange","Cherry","Mango","PineApple"]  
x[1]="watermelon"
print(x)

#change the range if item value in list. 
x=["Apple","Banana","Orange","Cherry","Mango","PineApple"]  
x[1:3]=["Watermelon","Chiku"]
print(x)

#change With one Value by Replacing with 2 Value
x=["Apple","Banana","Orange","Cherry","Mango","PineApple"]  
x[1:2]=["Watermelon","Nuts"]
print(x)
print(len(x))

#change With 2 value by replace with one value 
x=["Apple","Banana","Orange","Cherry","Mango","PineApple"] 
x[1:3]=["Watermelon"]
print(x)
print(len(x))
# user of replace Keyword

My_world="Welcome to My World"
new_world=My_world.replace("My","Our")
print(new_world)