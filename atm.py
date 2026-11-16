print("=======================")
print("WELCOME TO ATM")
print("=======================")

print("1.check Balance")
print("2.Withdraw Money")
print("3.Deposit Money")
print("4.Exit")

choice=input("Enter your choice:")
print("You selected:",choice)
balance=5000
if choice=="1":
    print("your current balance is:",balance)
elif choice=="2":
    amount=int(input("Enter withdrawl amount:"))

    if amount<= balance:
        balance=balance-amount
        print("Withdrawl successful!")
        print("Remaining balance:",balance)
    else:
        print("Insufficient balance!")

elif choice=="3":
    amount=int(input("Enter deposit amount:"))
    balance=amount+balance
    print("Deposit successful!")
    print("Update Balance:",balance)  

elif choice=="4":
    print("Thank you for using our ATM!")
    print("Have a nice day!")
pin="1234"

entered_pin=input("Enter your ATM pin:")
if entered_pin==pin:
    print("pin verification successfully!")
else:
    print("Incorrect")

pin="1234"
attemps=0
while attemps<3:
    entered_pin=input("Enter your ATM pin:")
    if entered_pin==pin:
        print("Pin verification successfully!")
        break
    else:
        attempts+=1
        print("Incorrect pin!")

    if attempts==3:
        print("ATM blocked.Too many attempts!")
        raise SystemExit


         
