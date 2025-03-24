# 🛠️ Project Requirements:
# Set an initial account balance (e.g., ₹10,000).

# Display menu options:
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit

# Perform transactions based on user input:
# If the user selects withdrawal, ensure the balance is sufficient.
# If the user selects deposit, add the amount to the balance.
# If the user selects check balance, display the current balance.
# If the user selects exit, stop the program.

account_balance = 10_000
print('''Enter your choice:
      1. Check Balance
      2. Deposit Money
      3. Withdraw Money
      4. Exit''')
while True:
    choice  = int(input("Press your choice: "))
    if choice == 1:
        print("Your current balance is",account_balance)
    elif choice == 2:
        amount = int(input("Enter the amount you want to deposit: "))
        account_balance+=amount
        print("Your account balance is",account_balance)
    elif choice == 3:
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount>account_balance:
            print("Insufficient balance...")
        else:
            account_balance-=amount
            print("Your account balance is",account_balance)
    elif choice == 4:
        print("Exited successfully")
        break