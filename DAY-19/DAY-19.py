# Inheritance
# 1)Single Inheritance
class A:
    def display(self):
        print("Parent class")
class B(A):
    def output(self):
        print("Child class")

b1=B()
b1.display()
b1.output()


# 2)Multilevel Inheritance
class A:
    def display(self):
        print("Parent class")
class B(A):
    def output(self):
        print("Child class")
class C(B):
    def greet(self):
        print("Hello World")

c1=C()
c1.display()
c1.output()
c1.greet()


# 3)Multiple Inheritance
class A:
    def display(self):
        print("Parent class")
class B:
    def output(self):
        print("Child class")
class C(A,B):
    def greet(self):
        print("Hello World")

c1=C()
c1.display()
c1.output()
c1.greet()

#task[take number in one class then print table of that number in other class[single level inheritance]]
class number:
    def __init__(self,num):
        self.num=num
 
class Table(number):
    def print_table(self):
        print(f"multiplication table of {self.num}:")
        for i in range(1,11):
            print(f"{self.num}x{i}={self.num*i}")

num=int(input("Enter a number:"))
obj=Table(num)
obj.print_table()

#task[create grading system[multilevel inheritance]]
# class value:
#     def __init__(self,num1,num2,num3,num4,num5):
#         self.num1=num1
#         self.num2=num2
#         self.num3=num3
#         self.num4=num4
#         self.num5=num5

# class total(value):
#         def print_total(self):
#             total=self.num1+self.num2+self.num3+self.num4+self.num5
#             print(f"total value are:{total}")

# class avg(total):
#      def print_avg(self,total):
#          avg=total/5
#          print(f"average are:{self.avg}")

# # class grade(avg):
# #     def print_grade(self):
# #         if self.avg>90:
# #             print(f"grade a")
# #         else:
# #             print("failing marks")

# show=total(10,20,30,40,50)
# show.print_total()
# show.print_avg(total)

#trying with other method
class num1:
    def eng(self,a):
        self.a=a

class num2(num1):
    def math(self,b):
        self.b=b

class num3(num2):
    def sci(self,c):
        self.c=c

class num4(num3):
    def pun(self,d):
        self.d=d

class num5(num4):
    def hin (self,e):
        self.e=e

    def total(self):
        total=self.a+self.b+self.c+self.d+self.e
        avg=total/5
        print(f"total are :{total}")
        print(f"average are :{avg}")
        if avg>90:
            print("GRADE A")
        elif avg>80:
            print("GRADE B ")
        elif avg>70:
            print("GRADE C ")
        elif avg>60:
            print("GRADE D")
        else:
            print("failing marks")

    # def avg(self):
    #     avg=total/5
    #     print(f"average are :{avg}")
    
    # def grade(self):
    #     if 

    
d1=num5()
d1.eng(95)
d1.math(90)
d1.sci(92)
d1.pun(98)
d1.hin(99)
d1.total()
# d1.avg()