# Conditional Statements

num=98
# 2)if-else Statement
if num < 90:
    print("Number is Smaller")
else:
    print("Number is Greater")


#task-1(if 2 number are equal to or not )
a=10
b=10
if a==b:
    print("a is equal to b")
else:
    print("a is not equal to b ")

 #task-2(if  number are odd or even)
c=2
if c%2==0:
    print("given number is even")
else:
    print("given number is odd")

#task-3 (greater or smaller)
d=10
if d<10:
    print("given number is greater")
else:
    print("given number is smaller")


# 3)elif
day=6
if day == 1 or day == 2 or day == 3 or day == 4 or day ==5:
    print("Weekday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid data")

#user input 
num=int(input("Enter any number"))
print(num)
print(type(num))

#task( take user input for subjects names  and calculate the avg )
eng=int(input("enter eng number"))
math=int(input("enter math number"))
hin=int(input("enter hin number"))
pun=int(input("enter pun number"))
sci=int(input("enter sci number"))
total=eng+math+hin+pun+sci
print(f"total obtained marks:{total}")
avg=total/5
if avg>90:
    print("grade A")
elif avg>80:
    print("grade B")
elif avg>70:
    print("grade C")
elif avg>60:
    print("grade D")
else:
    print("failing marks")

#task( elictricity bill in which take user input as units and print vill values)
units=int(input("enter number of units used:"))
if units >= 1 and units <= 600:
    print("bill is nil")
elif  units >= 601 and units <= 700:
    print(f"bill amount={units*3}")
elif  units >= 701 and units <= 800:
    print(f"bill amount={units*4}")
elif  units >= 801 and units <= 900:
    print(f"bill amount={units*5}")
else:
    print("consumption is too high")