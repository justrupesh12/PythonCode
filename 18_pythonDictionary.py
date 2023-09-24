#Ordered ,Changeable ,Not Accept Duplicate vale .
#Note :- Above Version #.7 All Dictionary is Ordered and below version is unordered .

#Difination of Dictionary
Rupesh={
    "brand":"Honda",
    "model":"DT",
    "year":2020
}
print(Rupesh)
#Output :- {'brand': 'Honda', 'model': 'DT', 'year': 2020}


#If you Want to print "brand" value from the Dictionary .
Rupesh={
    "brand":"Honda",
    "model":"DT",
    "year":2020
}
print(Rupesh["brand"])
print(type(Rupesh["brand"]))## return String Value


#Duplicate value will not Allowed it will Override with the last given Value

Rupesh={
    "brand":"Honda",
    "model":"DT",
    "year":2020,
    "year":2022
}
##Override With the new Value.
print(Rupesh)#{'brand': 'Honda', 'model': 'DT', 'year': 2022}

#Dictionary Length(This is also not Show the Duplicate value in length Also)
Rupesh={
    "brand":"Honda",
    "model":"DT",
    "year":2020,
    "year":2022
}
x=len(Rupesh)
print(x)# outPut 3

#Dictionary  items - Data Type
Rupesh={
    "brand":"Honda",
    "model":"DT",
    "year":2020,
    "color":["Red","White","Blue"]

}
print(Rupesh)

#How to Type of the function
print(type(Rupesh))

#Accessing Item of Dictionary
Rupesh={
    "brand":"Honda",
    "model":"DT",
    "year":2020,
}
x=Rupesh["brand"]
print(x)
#Accessing item through get() method
x=Rupesh.get("model")
print(x)

#key() method will return All the value of Dictionary

x=Rupesh.keys()
print(x)


#Add Item key to Original Dictionary

Rupesh={
    "brand":"Honda",
    "model":"DT",
    "year":2020,
}
x=Rupesh.keys()# before Add value in Key
Rupesh["Color"]="Orange"
print(x)
#Add value item to original Value
x=Rupesh.values()
print(x)# this is used for to get the value
Rupesh["Color"]="Blue"
print(x)

### How to get each items in a dictionary as a tuple inside list

Rupesh={
    "brand":"Honda",
    "model":"DT",
    "year":2020,
}
x=Rupesh.items()
print(x)
#output:- dict_items([('brand', 'Honda'), ('model', 'DT'), ('year', 2020)])

#### check the Key is Exist or not
Rupesh={
    "brand":"Honda",
    "model":"DT",
    "year":2020,
}
if "year" in Rupesh:
    print("Yes 'rupesh' is present in key")
