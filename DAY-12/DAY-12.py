#set method
my_set={"apple","banana",True,"mango","cherry","orange","banana",1, 0, False}
print(my_set)

#checking type
print(type(my_set))

#using for loop for set
for i in my_set:
    print(i)

#checking lenght of set
print(len(my_set))

#using if else for set
if "banana" in my_set:
    print("Found")
else:
    print("Not Found")

#adding data into set
my_set.add("plum")
print(my_set)

#updating data
s1={"a","b","c"}
s2={"A","B","C"}
s1.update(s2)
print(s1)

#removing data
my_set.remove("apple")
print(my_set)

#pop
my_set.pop()
print(my_set)

#deleting
# del my_set
# print(my_set)

#clear
my_set.clear()
print(my_set)

#task[take user input ask choice and perform all the operations for the given choice]
# new_set={"red","green","blue","yellow"}
# new_set1={1,2,3}
# print(new_set)
# print(new_set1)
# print("Press 1 for adding data into set")
# print("Press 2 for updating data from 2 sets")
# print("Press 3 for removing the data")
# print("Press 4 for pop the data item")
# print("Press 5 for deleting data item")
# print("Press 6 for clearing set")
# choice=int(input("enter the choice:"))
# if choice == 1:
#     data_item=input("enter the item name to add:")
#     new_set.add(data_item)
#     print(new_set)

# elif choice == 2:
#     new_set.update(new_set1)
#     print(new_set)

# elif choice == 3:
#     data_item=input("enter the data item name to remove:")
#     new_set.remove(data_item)
#     print(new_set)

# elif choice == 4:
#     new_set.pop()
#     print(new_set)

# elif choice == 5:
#     del new_set
#     print(new_set)

# elif choice == 6:
#     new_set.clear()
#     print(new_set)

# else:
#     print("invalid data")

#task[print prime number with the help of while loop]
new_set2={2,3,6,8}
for i in new_set2:
    # print(i)
    count=0
i=1
while i <= len(i):
   if new_set2%i==0:
    count+=1
    i+=1
