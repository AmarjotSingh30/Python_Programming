# File Handling
#used to write into file
# f=open("data.txt","w")
# f.write("How are you")
# print("Data saved in a file")
# f.close()

#used if you want previous data too
# f=open("data.txt","a")
# f.write(f"How are you\n")
# print("Data saved in a file")
# f.close()

#used to create file
# f=open("data.txt","x")
# f.write("How are you")
# print("Data saved in a file")
# f.close()

#used to read the data in a file
f=open("data.txt","r")
print(f.read())
f.close()

#task[take user input and print table of number into file]
a=open("table.txt","w")
num=int(input("enter the number:"))
for i in range(1,11):
    a.write(f"{num}x{i}={i*num}\n")
    # print("data saved into file")
a.close()

#task[take from user product name, price,quantity and print total and all user inputs into file]
b=open("product.txt","w")
product_name=input("ENTER THE PRODUCT NAME:")
product_price=int(input("ENTER THE PRODUCT PRICE:"))
product_quantity=int(input("ENTER THE QUANTITY NAME:"))
total=product_price*product_quantity
b.write(f"Product NAME is :{product_name}\n Product PRICE is :{product_price}\n Product QUANTITY is :{product_quantity}\n total is {total}")
print(f"data been saved")
b.close()