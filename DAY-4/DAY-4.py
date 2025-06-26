#task(find factorial number)
num1=6
fact=1
for i in range(1,num1+1):
    fact*=i
print(f"factorial of {num1} is {fact}")

#task(find prime number)
num=5
count=0
for i in range(1,num+1):
    if num%i == 0:
        count+=1
if count == 2:
    print(f"{num} is Prime")
else:
    print(f"{num} is Composite")

#task(find even number in range 81 to 100)
for i in range(81,100,1):
 if i%2==0:
    print(f"even number are:{i}")


# 2)while loop

i=1
while i<=10:
   print(f"{i} Amarjot Singh")
   i+=1

#task even number
i=1
while i <= 10:
   if i%2==0:
    print(f"even number are:{i}")
   i+=1

#task odd number
i=1
while i <= 10:
   if i%2!=0:
    print(f"odd number are:{i}")
   i+=1

#task print number from 31 to 50
i= 31
while i <=50:
   print(f"{i}")
   i+=1

#task (print number in reverse 200 to 181)
i=200
while i >= 181:
   print(f"{i}")
   i-=1

#task (sum of natural numbers 1 to 10)
sum=0
i=1
while i <= 10:
    sum+=i
    i+=1
print(f"the sum of  first ten natural number are: {sum}")

#task(print table of any number)
num9=2
i=1
while i<=10:
   print(f"{num9} x {i} = {num9*i} ")
   i+=1

#task( factorial number)
a=6
b=1
fact=1
while b<=a:
   fact*=b
   b+=1
print(f"factorial of {a} is {fact}")

#task ( find  prime numbers)
num=78
count=0
i=1
while i <= num:
   if num%i == 0:
      count+=1
   i+=1

if count == 2:
   print(f"{num} is Prime")
else:
    print(f"{num} is Composite")
   
#task( even number in range 81 to 100)
f=81
while f <= 100:
    if f%2==0:
        print(f"even number are : {f}")
    f+=1

