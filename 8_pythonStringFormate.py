#Wrong Method (Don't Use)

'''age =50
txt ="My Age is " + age
print(txt) '''
## Using Formate method for Concatination

''' age =50
txt ="My age is {}"
print(txt.format(age)) '''
##Format unlimited argument 
qty= 3
itemno=567
price=56.78
my_order="i want {} pices of item number {} of price {} rupee"
print(my_order.format(qty,itemno,price))

## formating unlimited argument with Indexting 
qty= 3
itemno=567
price=56.78
my_order="i want to pay {2} rupee for {0} pices of item number {1}"
print(my_order.format(qty,itemno,price))

