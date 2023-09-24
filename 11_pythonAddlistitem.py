# Append Function Use
x=["Apple","Banana","Orange"]
x.append("Cherry")
print(x)

# Insert Function
x=["Apple","Banana","Orange"]
x.insert(1,"Cherry")
print(x)
# Extend() FunCtion
x=["Apple","Banana","Orange"]
y=["Mango","Pineapple","Papaya"]
x.extend(y)
print(x)

#remove List item
x=["Apple","Banana","Orange"]
x.remove("Banana")
print(x)
#remove Specific index
x=["Apple","Banana","Orange"]
x.pop(1)
print(x)
#remove the last index without Knowing the length.
x=["Apple","Banana","Orange"]
x.pop()
print(x)

# Using Del For Specific index
x=["Apple","Banana","Orange"]
del x[0]
print(x)
# How to Del Whole List 
x=["Apple","Banana","Orange"]
del x
 
#clear the list method
x=["Apple","Banana","Orange"]
x.clear()
print(x)