txt="Python is a Fun language"
print(txt)
print(type(txt))

print(txt.upper())
print(txt.lower())
print(txt.casefold())
print(txt.capitalize())
print(txt.center(30,"-"))
print(txt.endswith("e"))
print(txt.find("a"))
print(txt.replace("P","J"))
print(txt.index("n"))
print(txt.count("a"))
print(txt.startswith("P"))

#slicing
print(txt[2:6])
print(txt[:6])
print(txt[2:])

#print statement in the same way it writes below
para="""
    Python is
    Fun
            Language
"""
print(para)
print(len(txt))
for i in range(0,len(txt)):
    print(txt[i])

if "is" in txt:
    print("Found")
else:
    print("Not Found")

print(txt[8])

#task[take user input for string]
# txt1=input("enter the string:")
# choice=input("enter the word you want to search:")
# if choice in txt1:
#         print("found")
# else:
#     print("not found")

#task[to print patter of "*"]
for i in range(1,6):
    for j in range (1,9):
        if(i== 1 or j == 1 or i ==5 or j== 8):
            print(" * ",end=" ")
        else:
            print("   ",end=" ")
    print()
  

