# class
class greet:
    def display(self):
        print("Hello World")

g1=greet()#constructor
g1.display()


class add:
    #default method
    def __init__(self,name,marks,city):
        self.name=name
        self.marks=marks
        self.city=city
    #2nd method
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"City: {self.city}")

    #string method
    def __str__(self):
        return f"{self.name} {self.marks} {self.city}"

a1=add("Rahul",89,"Khanna") #data used by default method
a1.display() #display data of 2nd method

print(a1)

#task[take user input and print table ]
num=int(input("enter the number you wanna print table of:"))
class table:
    def __init__(self,number):
        self.number=number
    def show(self):
        for i in range(1,11):
            print(f"{num}x{i}={i*num}")

a2=table(num)
a2.show()

#task[print prime number]
class prime:
    def __init__(self,number):
        self.number=number
    def show1(self):
        count=0
        for i in range(1,(self.number)+1):
            if self.number%i==0:
                count+=1
        if count == 2:
                print(f"{self.number} is prime number")
        else:
                print(f"{self.number} is composite number")
a3=prime(5)
a3.show1()
