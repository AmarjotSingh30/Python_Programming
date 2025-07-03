# List Methods
my_list=["apple","mango","banana","watermelon","plum"]
print(my_list)

#inserting
my_list.insert(2,"cherry")
print(my_list)

#append
my_list.append("melon")
print(my_list)

#remove
my_list.remove("mango")
print(my_list)

#pop at index
my_list.pop(3)
print(my_list)

#pop 
my_list.pop()
print(my_list)

#deleting
# del my_list
# print(my_list)

#sorting
my_list.sort()
print(my_list)

#reverse sorting
my_list.sort(reverse=True)
print(my_list)

#clearing
# my_list.clear()
# print(my_list)

#reverse
my_list.reverse()
print(my_list)

#task[provide option to users and perform operation of above list methods]
new_list=["red","blue","green","purple"]
print(new_list)
print("Press 1 for inserting at index in list")
print("Press 2 for insert  item in list at end ")
print("Press 3 for delete  item in list")
print("Press 4 for sorting a list in (ascending order)")
print("Press 5 for sorting list in reverse(descending order)")
print("Press 6 for clearing list")
print("Press 7 for reverse  list")
choice=int(input("enter the choice:"))
if choice == 1:
    index_value=int(input("enter the index value:"))
    item_name=input("enter the item name:")
    new_list.insert(index_value,item_name)
    print(new_list)

elif choice == 2:
    item_name=input("enter the item name:")
    new_list.append(item_name)
    print(new_list)

elif choice ==3:
    index_value=int(input("enter the index value:"))
    new_list.pop(index_value)
    print(new_list)

elif choice == 4:
    new_list.sort()
    print(new_list)

elif choice == 5:
    new_list.sort(reverse=True)
    print(new_list)

elif choice == 6:
    new_list.clear()
    print(new_list)

elif choice == 7:
    new_list.reverse()
    print(new_list)

else:
    print("invalid choice")