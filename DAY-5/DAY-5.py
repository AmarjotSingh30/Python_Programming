# Nested loops
for i in range(1,6): #Rows
    for j in range(1,6): #Columns
        print(" * ",end=" ")
    print()

# task (1) to print pattern * (3(rows)x8(columns))
for i in range (1,4):
    for j in range (1,9):
        print(" * ",end="")
    print()

# task (2) to print pattern of [*] 
for i in range (1,6):
    for j in range (1,i+1):
        print(" * ",end=" ")
    print()

#task (3) to print pattern of [1,2,3,4,5]
for i in range (1,6):
    for j in range(1,i+1):
        print(f"{j}",end=" ")
    print()

# task (4)to print pattern [1,2,3,4,5]
for i in range(1,6):
    for j in range(1,i+1):
        print(f"{i}",end=" ")
    print()

#task (5) to print pattern [1,2,3,4,5]
a=1
for i in range(1,6):
    for j in range(1,i+1):
        print(f"{a}",end=" ")
        a+=1
    print()

#task (6) to print  [*]
for i in range(1,6):
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()

#task (7) to print pattern [1,2,3,4,5]
for i in range(1,6):
 for j in range(1,6):
     print(f"{i*j}",end=" ")
 print()

#pattern of [*] (5 rows x 5 columns) with while loop 
i=1 #row
while i<=5:
    j=1 #column
    while j<=5:
        print(" * ",end=" ")
        j+=1
    print()
    i+=1

#task(1) to print [*] with 3(row)x8(column)
i=1
while i<=3:
    j=1
    while j<=8:
        print("*",end=" ")
        j+=1
    print()
    i+=1

#task(2) to print [*]
i=1
while i <= 5:
    j=1
    while j <= i:
        print("*",end=" ")
        j+=1
    print()
    i+=1

#task(3) to print[1,2,3,4,5]
i=1
while i<=5:
    j=1
    while j<=i:
        print(f"{j}",end=" ")
        j+=1
    print()
    i+=1

#task(4) to print pattern of [1,2,3,4,5]
i=1
while i<=5:
    j=1
    while j<=i:
     print(f"{i}",end=" ")
     j+=1
    print()
    i+=1

#task(5) to print pattern of [1,2,3,4,5]
b=1
i=1
while i<=5:
    j=1
    while j<=i:
        print(f"{b}",end=" ")
        j+=1
        b+=1
    print()
    i+=1

#task(6) to print pattern [*]
i=1
while i<=5:
    j=5
    while j >= i:
        print("*",end=" ")
        j-=1
    print()
    i+=1

#task(7) to print pattern of [1,2,3,4,5]
i=1
while i<=5:
    j=1
    while j<=5:
     print(f"{i*j}",end=" ")
     j+=1
    print()
    i+=1