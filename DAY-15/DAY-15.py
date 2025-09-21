#simple function
def greet():
    print("Hello World")

#function with argument and parameter
def add(a,b): #parameter
    print(f"Addition: {a+b}") #argument

#return function
def multi(a,b): 
    return a*b
    
greet() #calling function
greet()
add(44,77)
greet()
print(f"Multiplication: {multi(44,22)}")#return function output
add(78,33)
greet()
greet()
add(44,77)

#task[take a user input which prints table with help of function]
def table(a):
    # a=int(input("enter the number whos table wanna print:"))
    for i in range(1,11):
         print(f"multiplication of :{a}x{i}={i*a}")

table(a=int(input("enter the number whos table wanna print:")))

#task[pass 5 arguments and calculate their total and avg then print grades]
def grade(eng,math,sci,pun,hin):
    total=eng+math+sci+pun+hin
    print(f"total number are:{total}")
    avg=total/5
    print(f"average number are:{avg}")
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

grade(20,40,50,60,46)
grade(eng=int(input("enter the english number:")),
    math=int(input("enter the math number:")),
    sci=int(input("enter the science number:")),
    pun=int(input("enter the punjabi number:")),
    hin=int(input("enter the hindi number:")))