#Loop Through Dictionary

Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
for i in Rupesh:
    print(i)
# With looping the All the value  in the Dictionary one by one\
Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
for i in Rupesh:
    print(Rupesh[i])

#Value() will Reture all the value of Dictionary
Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
for i in Rupesh.values():
    print(i)

#Key() methot to retured the key valuse of Dictionary 
Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
for i in Rupesh.keys():
    print(i)
# Now Loop through both the key and value by using Items() method
Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
for i in Rupesh.items():
    print(i)  

#another Way by using two variable 
Rupesh={
    "brand":"Farari",
    "model":"XYZ",
    "year":2020,
}
for i , y in Rupesh.items():
    print(i ,y )    
# How to Copy Dictionary
Rupesh={
    "brand":"Farari",
    "model":"XYZ",
    "year":2020,
}
Rupesh1=Rupesh.copy()
print(Rupesh1)

#another way to copy by using dict() method. Build in Function
Rupesh={
    "brand":"Farari",
    "model":"XYZ",
    "year":2020,
}
    
Rupesh1=dict(Rupesh)
print(Rupesh1)

#Nested Dictionary:-a Dict an Able to COntain Another Dictonary 
myfamily={
    "child1":{"name":"Ram","year":"10"},
    "child2":{"name":"laxma","year":"8"},
    "child3":{"name":"bharat","year":"6"},
}
print(myfamily)
#if you want to Add new Dictionary in new Dict
child1={"name":"Ram",
        "year":"10"
        },
child2={"name":"laxma",
        "year":"8"
        },
child3={"name":"bharat",
        "year":"6"
         }

mybaby={
    "papa1" :child1,
    "papa2":child2,
    "papa3":child3 
}
print(mybaby)