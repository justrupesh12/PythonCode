## How To change the Value in Dictionary

Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
Rupesh["brand"]="TVS"
print(Rupesh)


## Using Update method
Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
Rupesh.update({"year":"2018"})
print(Rupesh)

## How To Add item in Dictionary
Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
Rupesh["Color"]="Red"
print(Rupesh)

## Adding the item With update() method

Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
Rupesh.update({"Color":"Blue"})
print(Rupesh)

## Removing the ITem From the Dictionary
Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
Rupesh.pop("model")
print(Rupesh)

##remove last inserted item in Dictionary
Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
Rupesh.popitem()
print(Rupesh)

##Del() keyWord the item with the Specific key name

Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
del Rupesh["brand"]
print(Rupesh)
## Del () Also delete whole Dictionary
Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
del Rupesh
## Clear user to Empty the Dictionary 

Rupesh={
    "brand":"Honda",
    "model":"XYZ",
    "year":2020,
}
Rupesh.clear()
print(Rupesh)

