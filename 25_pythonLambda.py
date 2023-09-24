## Lambda 

x =lambda a:a+10
print(x(5))

# lambda function can take multiple argument

x=lambda a,b:a*b
print(x(5,6))

#Why lambda Function  Fo Double And Triple

def my_Function(n):
    return lambda a:a*n

myDouble=my_Function(2)
mytriple=my_Function(3)
print(myDouble(11))
print(mytriple(11))