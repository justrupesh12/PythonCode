#What are python
#1.unchangable,unorderd,no indexed ,no Duplicate


x ={"pappu","Mahato","takla"}
print(x)
#Duplicate is not allowed
x={"a","b","c","a"}
print(x) # Returen Abc in unorder manner 

#get the lenth of set
x ={"pappu","Mahato","takla"}
print(len(x))

#How to check Data type of Set
set1={"a","b","c"}
set2={1,2,3}
set3={True,False,True}
print(type(set1))
print(type(set2))
print(type(set3))

#A set with All String Booleans,integer and all Data type

set1={"Apple",2,True,10,'male'}
print(set1)

# The Set() Constructor
thisset =set(("a","b","c"))
print(thisset)
print(type(thisset))

# Adding is possible in Set by Uaing ADD() method
set1={"a","b","c"}
set1.add("lolipop")
print(set1)
#How to Access item in Set 
set1={"a","b","c"}
for i in set1:
    print(i)

# Check is any item is present in Set
x ={"pappu","Mahato","takla"}
print("takla" in x)   # Return Boolean Value

#Note :- Add and update 

# how to Add item from another set into the Current set 
# Adding is possible in Set by Uaing ADD() method
name ={"Ram","Rohit","Pappu"}
diwana={"Pyar","Diwana","Hota"}
name.update(diwana)
print(name)

#How to Remove the set items (Discard() and remove Both are used for Remove )

name ={"Ram","Rohit","Pappu"}
name.remove("Ram")
print(name)

#How to use discard to remove the item from Set 
name ={"Ram","Rohit","Pappu"}
name.discard("Rohit")
print(name)

## Don't Use pop its a bad practice . This is always remove the last element From the Set
#For Example 
name ={"Ram","Rohit","Pappu"}
name.pop()
print(name)# In Set is not define which element will remove because it is and unorderd Data type.

# How to use Clear() method .This is normally use for empty the Set 
name ={"Ram","Rohit","Pappu"}
name.clear()
print(name)

#Use of del Keyword 
name ={"Ram","Rohit","Pappu"}
del name

#How to Loop through the Set 
name ={"Ram","Rohit","Pappu"}
for i in name:
    print(i)

# How to Joins Two Set ?
# Sets can be Joins by using Union() method and Update () method 
# But the Different is Update() methond can ben Define in present vaiable  and Union() method Can be Joined in the new variable 

#Example of update
name ={"Ram","Rohit","Pappu"}
number ={1,2,3}
name.update(number)
print(name)
#Example of Union

name ={"Ram","Rohit","Dharo"}
number ={1,2,3}
set1=name.union(number)
print(set1)

#Keep only Dunlicate item only by using Intersection_update() method
name1 ={"Ram","Gulabo","Dharo"}
name2 ={"Ram","Rohit","Pappu"}
name1.intersection_update(name2)
print(name1)
#intersection() method with return new set for Common and Duplicate Value
name1 ={"Pappu","Gulabo","Dharo"}
name2 ={"Ram","Rohit","Pappu"}
name3=name1.intersection(name2)
print(name3)

#Keep All but not the Common and Duplicate ITEMs symmetric_difference_update()
name1 ={"Pappu","Gulabo","Dharo"}
name2 ={"Ram","Rohit","Pappu"}
name1.symmetric_difference_update(name2)
print(name1)

#symmetric_difference() method Will Return a new set that Contain only the element Which is not present in both sets
name1 ={"Pappu","Gulabo","Dharo"}
name2 ={"Ram","Rohit","Pappu"}
name3=name1.symmetric_difference(name2)
print(name3)

# All Python BUILTIN Set method
# add()
# clear()
# copy()
# difference_update()
# discard()
# intersection()
# intersection_update()
#pop()
#Remove()
#union()
#update()
#Symmetric_Difference()
#Symmetric_Difference_update()

