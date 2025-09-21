#tuples
my_tuple=("apple","mango","banana","watermelon","apple") #we can take duplicate values in tuples
print(my_tuple)
print(type(my_tuple)) 

# my_tuple[1]="plum" throwing error because we cannot update tuple
# print(my_tuple)

print(my_tuple.index("banana")) #telling index value or position  
print(my_tuple.count("apple")) #counting how man data items are present

#using for loop for tuple
for i in my_tuple:
    print(i)

#using if else in tuple
if "mango" in my_tuple:
    print("found")
else:
    print("not found")

#using while loop in tuple
i=0
while i<len(my_tuple):
    print(my_tuple[i])
    i+=1

#printing with index values
print(my_tuple[0])
print(my_tuple[-1])

#slicing
print(my_tuple[2:4])
print(my_tuple[:4])
print(my_tuple[2:])

#storing tuples data in variables [unpacking the tuple data items]
a,b,c,d,e=my_tuple
print(a)
print(b)
print(c)
print(d)
print(e)

#adding two tuples
a1=("R","a","h","u","l")
a2=("K","u","m","a","r")
a3=a1+a2
print(a3)

#tuple functions
marks=(66,88,44,33,55,66,77)
print(sum(marks))
print(max(marks))
print(min(marks))

#task [provide multiple user options for different tuple functions ]
new_tuple=(22,45,50,60,99)
new_tuple1=(33,44,55,66,77)
print(new_tuple)
print(new_tuple1)
print("press 1 for sum")
print("press 2 for finding maximum number")
print("press 3 for finding minimum number")
print("press 4 for adding two tuples")
print("press 5 for finding index value of particular data item")
print("press 6 for counting how many times data item comes in tuple")
choice=int(input("enter the choice:"))
if choice == 1:
    print(sum(new_tuple))
    print(sum(new_tuple1))

elif choice == 2:
    print(max(new_tuple))

elif choice == 3:
    print(min(new_tuple))

elif choice == 4:
    print(new_tuple+new_tuple1)

elif choice ==5:
    find_tuple=int(input("enter the data item to find the index value:"))
    print(new_tuple[find_tuple])

elif choice ==6:
    data_item=int(input("enter the data item to count:"))
    print(new_tuple.count(data_item))

else:
    print("invalid data")