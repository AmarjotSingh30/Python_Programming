#task[to check prime number and composite number in a list]
new_list=[2,5,99,20,35]
for i in new_list:
    count=0
    for j in range(1,i+1):
        if i%j == 0:
            count+=1
    if count == 2:
        print(f"{i} is prime number")
    else:
        print(f"{i} is composite number")

#task[to find factorial of number]
new_list1=[1,2,3,4,5]
for i in new_list1:
    fact=1
    for j in range(1,i+1):
        fact*=j
    print(f"factorial of {i} is {fact}")

#task[print table of number]
new_list2=[2,4,6,8]
for i in new_list2:
    for j in range(1,11):
        print(f" table of {i} x {j} = {i*j} ")

#task[print odd numbers]
new_list3=[2,7,5,3]
for i in new_list3:
    if i%2!=0:
        print(f"odd numbers are:{i}")