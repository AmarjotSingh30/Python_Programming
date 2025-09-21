# Multilevel Inheritance

class A:
    def inputA(self,a):
        self.a=a

class B(A):
    def inputB(self,b):
        self.b=b

class C(B):
    def inputC(self,c):
        self.c=c

    def addition(self):
        print(f"Addition: {self.a+self.b+self.c}")

c1=C()
c1.inputA(67)
c1.inputB(58)    
c1.inputC(49) 
c1.addition()   

# 4)Hierarchical Inheritance
class A:
    def inputA(self,a):
        self.a=a
class B(A):
    def inputB(self,b):
        self.b=b
        print(f"Add: {self.a+self.b}")
class C(A):
     def inputC(self,c):
        self.c=c
        print(f"Product: {self.a*self.c}")
    
b1=B()
c1=C()
b1.inputA(45)
b1.inputB(55)

c1.inputA(44)
c1.inputC(33)


# Overriding

class A:
    def display(self):
        print("Parent class")
class B(A):
    def display(self):
        print("child class")
    
b1=B()
b1.display()

# Polymorphism(pending)
class A:
    def add(self,a,b):
        self.a=a
        self.b=b
        print(f"Addition of A and B: {self.a+self.b}")

    def add(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(f"Addition of A, B and C: {self.a+self.b+self.c}")
    
a1=A()
a1.add(44,77)
a1.add(44,77,45)


