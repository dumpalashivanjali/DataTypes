print("----ATM----")
print("""1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit""")

current_balance = 5000
while True:
    choice = int(input("Please choose an option: "))
    if choice == 1:
        print(f"Current Balance : {current_balance}")
    elif choice ==2:
        amount= int(input("Please enter the amount to deposit:"))
        current_balance+=amount
        print("Amount Deposited")
    elif choice==3:
        withdraw_amount=int(input("Please enter the amount to withdraw: "))
        if withdraw_amount <=current_balance:
            current_balance-=withdraw_amount
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")
    elif choice==4:
        break
    else:
        print("Please enter a valid choice!")

print(f"Current Balance: {current_balance}")


