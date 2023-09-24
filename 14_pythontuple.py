#(Very improtant ) Changeing the value of Tuple with the help of list 
x=("Rupesh","Banana","orange","Cherry","Papaya","Kiwi","Orange","Nuts","Kumar")
print(type(x))
y=list(x)
print(type(y))
y[1]="Python"
x=tuple(y)
print(x)
print(type(x))
# Add item in tuple
x=("Rupesh","Banana","orange","Cherry","Papaya","Kiwi","Orange","Nuts","Kumar")
print(type(x))
y=list(x)
print(type(y))
y.append("Last value")
print(y)
x=tuple(y)
print(x)

#Add tuple to a tuple
x=("Apple","Banana","Orange")
y=("Kiwi",)
x+=y
print(x)
print(type(x))
#Remove item from tuple
x=("Rupesh","Banana","orange","Cherry","Papaya","Kiwi","Orange","Nuts","Kumar")
print(type(x))
y=list(x)
print(type(y))
y.remove("Kumar")
x=tuple(y)
print(type(x))
print(x)
#How to delete tuple
#yes we can delete the tuple 
x=("Rupesh","Banana","orange","Cherry","Papaya","Kiwi","Orange","Nuts","Kumar")
del x

#Packing a Tuple (When we assigned value to tuple)
x=("Rupesh","kumar","Banana")
#unpacking the tuple (when we extact the value from Tuple)
x=("Rupesh","kumar","Banana")
(green,yellow,red)=x
print(green)#Rupesj
print(yellow)#Kumar
print(red)#Banana 


#How to Assign the rest of the value in tuple

x=("Rupesh","kumar","Banana","Kiwi","Apple")
#(green,yellow,red)=x  #we need to Add * in the Front of last value So rest value will Assigned in the last variable in form of "LIST" Example below
(green,yellow,*red)=x 
print(green)#Rupesj
print(yellow)#Kumar
print(red)#["Banana","Kiwi","Apple"] in form of list
