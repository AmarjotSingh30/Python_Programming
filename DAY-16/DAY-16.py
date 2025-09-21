#task[find prime number from argument with return function ]
def prime(a):
    count=0
    for i in range(1,a+1):
        if a%i == 0:
            count+=1
    return count    

r=prime(9)
if r == 2:
    print("Prime number")
else:
    print("Composite")


# Filter function
my_list=[66,88,44,33]
def is_even(number):
    return number%2 == 0

ev=list(filter(is_even,my_list))
print(ev)

# Lambda Function
my_list=[66,88,44,33]

ev=list(filter(lambda number: number%2 == 0,my_list))
print(ev)

#task[create a filter function that user number from list and print grades according to it]+map function
grade_list=[99,55,77,44,55,66,77,99]
def is_num(number):
    if number > 90:
        return "A"
    elif number > 80:
        return "B"
    elif number > 70:
        return "C"
    elif number >= 60:
        return "D"
    else: 
        return "Fail"
marks=list(map(is_num,grade_list))
print(marks)

#understanding the working of classes and objects
class A:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def greet(self):
        print("Hello")
        print(f"Hello! {self.name}")
        print(f"You got: {self.marks}")


a1=A("rahul",89)
a1.greet()
