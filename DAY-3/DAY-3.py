# # Nested if
# x,y,z=78,54,67

# if x > y:
#     if x > z:
#         print("X is Greatest")
#     else:
#         print("Z is Greatest")
# else:
#     if y > z:
#         print("y is Greatest")   
#     else:
#         print("Z is Greatest")

# #task(take 3 number from user and check which is smallest)
# num1=int(input("enter number 1:"))
# num2=int(input("enter number 2:"))
# num3=int(input("enter number 3:"))
# if num1<num2:
#     if num1<num3:
#         print("num1 is smallest")
#     else:
#         print("num3 is smallest")
# else:
#     if num2<num3:
#         print("num2 is smallest")
#     else:
#         print("num3 is smallest")

# #task( take 2 user input and ask for choice to perform operation on 2 number acccording to choice)
# x=int(input("enter x value:"))
# y=int(input("enter y value:"))
# print("Enter 1 for Addition")
# print("Enter 2 for subtraction")
# print("Enter 3 for multiplication")
# print("Enter 4 for division")
# choice=int(input("enter your choice:"))
# if choice == 1:
#     print(f"Addition of x and y {x+y}")
# elif choice == 2:
#     print(f"Subtraction of x and y {x-y}")
# elif choice == 3:
#     print(f"Multiplication of x and y {x*y}")
# elif choice == 4:
#     print(f"Division of x and y {x/y}")
# else:
#     print("Invalid data")


# Looping Statements
# 1)for loop
# 2)while loop

for i in range(1,11,1):
    print(f"{i} Amar")

for i in range(1,11,1):
    print(f"{i} Amar")

#increment by 2
for i in range(1,11,2):
    print(f"{i} Amar")
#increment by 2 
for i in range(2,11,2):
    print(f"{i} Amar")

#task ( print number from 31 to 50)
for i in range (31,51):
    print(f"{i}")

#task( print number in reverse from 181 to 200)
for i in range(200,180,-1):
    print(f"{i}")

#task print sum of natural number 1 to 10
sum=0
for i in range(1,11):
    sum+=i
print(f"Sum of first ten natural numbers= {sum}")


#task print table of any number
num=6
for i in range (1,10):
    print(f"{num} x {i} = {i*num}")