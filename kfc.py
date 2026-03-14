def display_menu():
    print("------ KFC MENU ------")
    print("1. Burger  - 120")
    print("2. Fries   - 80")
    print("3. Coke    - 50")
    print("4. Chicken - 200")
    print("0. Exit")
display_menu()

total_bill = 0
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Burger added to order")
        total_bill += 120
    elif choice == 2:
        print("Fries added to order")
        total_bill += 80
    elif choice == 3:
        print("Coke added to order")
        total_bill += 50
    elif choice == 4:
        print("Chicken added to order")
        total_bill += 200
    elif choice == 0:
        break
    else:
        print("Invalid!")

print("Total Bill:", total_bill)
print("Thank you for ordering!")