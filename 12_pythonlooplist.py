#Loop through List
list= ["Rupesh", "Pappu","Manish"]
for i in list:
    print(i)

# Loop Through lindex number (Range ,length)

list=["Rupesh","manish","Rohan,,,"]
for i in range(len(list)):
    print(list[i])

#Using While Loop
list=["Rupesh","manish","Rohan"]
i=0
while i <len(list):
    print(list[i])
    i=1+i
#looping Using the list Comprehension
list=["Rupesh","manish","Rohan"]
[print(i) for i in list]

#List Comprehension
fruits=["Rupesh","banana","orange","Cherry","mango","Kiwi"] 
newlist=[]
for i in fruits:
    if "a" in i:
        newlist.append(i)
print(newlist)     

#list Comprehension in 1 line 
fruits=["Rupesh","banana","orange","Cherry","mango","Kewi"] 
newlist=[ i for i in fruits if "e" in i]
print(newlist)

#note first i represent expresion
#for means for loop 
#next i is an item 
#in for checking purpose
#fruits is called as item
#if "e" which represents Condition 
# in i  that Should be operaror 