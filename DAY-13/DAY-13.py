# Dictionary

my_dict={
    'name':'Rahul',
    'age':26,
    'city':'Khanna',
    'Marks':89,
    'class':'BCA' 
}
print(my_dict)

#checking type
print(type(my_dict))

#checking data with its key
print(my_dict['city'])

#adding data into dictionary
my_dict['state']='Punjab'
print(my_dict)

#updating data
my_dict['Marks']=98
print(my_dict)

#checking only key
for key in my_dict:
    print(key)

#checking only values
for value in my_dict.values():
    print(value)

#checking both key and values
for key,value in my_dict.items():
    print(f"{key} = {value}")

#getting data
print("city" in my_dict)

#checking data if its present in dictionary
print(my_dict.get("state"))

#clearing
my_dict.clear()
print(my_dict)

#task(provide user option to add data at specific key and delete data from dictionary)
# new_dict={
#      'name':'jerry',
#      'class':'BBA'
#       }
# print(new_dict)
# print("press 1 for adding data into dictionary")
# print("press 2 for deleting data")
# choice=int(input("enter the choice:"))
# if choice == 1:
#     key=input("enetr the key name:")
#     value=input("enter the data item:")
#     new_dict[key]=value
#     print(new_dict)

# elif choice == 2:
#     new_dict.clear()
#     print(new_dict)

# else:
#     print("invalid data")

#task[create a resturant system that provide multiple snacks options and show total prize of snacks]
rest_dict={
    'pizza':100,
    'burger':80,
    'patty':40,
    'wrap':100
}
sum=0
while True:
    choice=input("enter the item number:")
    if choice in rest_dict:
        sum+=rest_dict[choice]
    else:
        print("item is not in the list")

    cn=input("do you want to order more:")
    if cn.lower()!="yes":
        print(f"your total order is {sum}")
        break
