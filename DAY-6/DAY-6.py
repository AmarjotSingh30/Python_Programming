#task (1) to print patter [*]
for i in range(1,6):
    for j in range(1,6-i):
      print(" ",end=" ")
    for k in range (1,i+1):
           print("*",end=" ")
    print()

#task(2) to print pattern of [*]
for i in range (1,6):
  for j in range(1,6-i):
    print(" ",end=" ")
  for k in range(1,(i*2+1)-1):
    print("*",end=" ")
  print()

#task(3) to print pattern of [1,2,3,4,5]
for i in range (1,6):
  for j in range(6,i-1,-1):
    print(f"{i}",end=" ")
  print()

for i in range (1,6):
  for j in range(1,(6-i)+1):
    print(f"{j}",end=" ")
  print()
