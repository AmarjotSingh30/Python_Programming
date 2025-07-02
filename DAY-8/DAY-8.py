#revise task 
for i in range(1,6):
    for j in range(1,9):
        if (i == 1 or j == 1 or i == 5 or j == 8):
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
    print()


# List
my_list=[34,74,22,77,32,44,88,66,12,44,65]
print(my_list)
print(type(my_list))

print(len(my_list))
print(my_list[3])
print(my_list[-1])
print(my_list[4:8])
print(my_list[:8])
print(my_list[4:])

#updating value in list
my_list[10]=78
print(my_list)

#adding value in list 
my_list.append(89)
print(my_list)

# for printing list value one by one 
for i in my_list:
    print(i)

#practice 
todo_list=["1.buy snakcks","2.go home",20,20.9,"english","punjabi"]
print(todo_list) 
print(todo_list[3])
todo_list.append("hello")
print(todo_list)
todo_list[4]="french"
print(todo_list)

#task[create a list of numbers and print sum of numbers in the list]
sum=0
num_list=[1,2,3,4,5]
for i in num_list:
    sum+=i
print(f"sum of number are ={sum}")

#task[find even numbers in list]
new_list=[21,30,90,109,120,200,320]
for i in new_list:
    if i%2==0:
        print(f"even numbers are:{i}")

    





