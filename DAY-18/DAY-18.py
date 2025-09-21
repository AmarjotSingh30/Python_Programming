#ATM MACHINE
balance=18000

#function
#2)choice == 2 ()
def withdraw():
    global balance #setting balance to global because it is outside the function
    withdraw=int(input("enter the amount to withdraw:"))
    if withdraw>balance:
        print(f"insufficent balance ")
    else:
        balance-=withdraw #to update balance
        print(f"balance left is {balance}")

#3)choice == 3 (deposit)
def deposit():
    global balance #setting balance to global because it is outside the function
    deposit=int(input("ENTER THE AMOUNT TO ADD INTO ACCOUNT:"))
    balance+=deposit
    print(f"{deposit} is added to balance,total balance is {balance}")
#function

#authentication
attempts=0
while attempts < 3:
    card_number=int(input("ENTER THE CARD NUMBER:"))
    if card_number == 1234:
        pin_number=int(input("ENTER THE PIN:"))
        if pin_number == 0000:
#authentication
            while True:
                print(f"PRESS 1 TO CHECK BALANCE")
                print(f"PRESS 2 TO WITHDRAW MONEY")
                print(f"PRESS 3 TO DEPOSIT MONEY")
                print(f"PRESS 4 TO EXIT")

                choice=int(input("ENTER THE CHOICE:"))

                if choice == 1:
                    print(f"balance is {balance}")

                elif choice == 2:
                    withdraw()
                    # withdraw=int(input("enter the amount to withdraw:"))
                    # if withdraw>balance:
                    #     print(f"insufficent balance ")
                    # else:
                    #     balance-=withdraw #to update balance
                    #     print(f"balance left is {balance}")

                elif choice == 3:
                    deposit()
                    # deposit=int(input("ENTER THE AMOUNT TO ADD INTO ACCOUNT:"))
                    # balance+=deposit
                    # print(f"{deposit} is added to balance,total balance is {balance}")

                elif choice == 4:
                    print(f"EXIT")
                    break

                else:
                    print(f"INVALID DATA")
        else:
            print(f"INVALID PIN")
            attempts+=1
    else:
        print(f"INVALID CARD NUMBER")
        attempts+=1

    if attempts ==3:
        print(f"your account is blocked due to 3 multiple wrong attempts")
        break
    
