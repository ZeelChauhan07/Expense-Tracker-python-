# EXPENSE TRACKER

import json
import os

print("Welcome to the Expense Tracker!")
expenses = []

ExpenseTracker = "expenses.json"


# ADD EXPENSE
def one():
    date = input("Date (DD-MM-YYYY): ")
    category = input("Category: ")
    description = input("Description: ")
    amount = float(input("Amount: "))
    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    save_data()
    print("Expense added successfully!\n\n")

# VIEW EXPENSES
def two():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Date\t\tCategory\tDescription\tAmount")
        for expense in expenses:
            print(f"{expense['date']}\t\t{expense['category']}\t\t{expense['description']}\t\t{expense['amount']}")
            #  print(f"{expense['amount']}")

# VIEW ALL DETAILS
def three():
    if not expenses:
        print("No expenses recorded.")
    else:
        total_amount = sum(expense['amount'] for expense in expenses)
        print("Date\t\tCategory\tDescription\tAmount")
        for expense in expenses:
            print(f"{expense['date']}, {expense['category']}, {expense['description']}, {expense['amount']}")
      
        print(f"Total Amount: {total_amount}")

# EXIT
def four():
    save_data()
    print("Exiting..")


# Load data
if os.path.exists(ExpenseTracker):
    with open(ExpenseTracker, "r") as file:
        expenses = json.load(file)
else:
    expenses = []


def save_data():
    with open(ExpenseTracker, "w") as file:
        json.dump(expenses, file, indent=4)


while True:
    print("-------Menu-------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View all details")
    print("4. Exit\n")
   
    choice = int(input("Enter your choice (1-4): "))
    if choice == 4:
        break
    elif choice < 1 or choice >4:
        print("Invalid choice ")
    elif(choice == 1):
        one()
        print("Expense added successfully!\n\n")
    elif(choice == 2):
        two()
    elif(choice == 3):
        three()
    elif(choice == 4):
        four()
    else:
        print("Invalid choice")


print("Thank you for using the Expense Tracker!")

