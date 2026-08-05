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
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense['date']}\t\t{expense['category']}\t\t{expense['description']}\t\t{expense['amount']}")


# UPDATE EXPENSE
def three():
    if not expenses:
        print("No expenses recorded.")
        return

    two()
    try:
        index = int(input("Enter the expense number to update: "))
    except ValueError:
        print("Invalid expense number.")
        return

    if index < 1 or index > len(expenses):
        print("Expense number out of range.")
        return

    print("Enter the new expense details to replace the selected record.")
    date = input("New date (DD-MM-YYYY): ")
    category = input("New category: ")
    description = input("New description: ")
    amount = float(input("New amount: "))

    new_expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses[index - 1] = new_expense
    save_data()
    print("Expense updated successfully!\n\n")


# DELETE EXPENSE
def four():
    if not expenses:
        print("No expenses recorded.")
        return

    two()
    try:
        index = int(input("Enter the expense number to delete: "))
    except ValueError:
        print("Invalid expense number.")
        return

    if index < 1 or index > len(expenses):
        print("Expense number out of range.")
        return

    removed_expense = expenses.pop(index - 1)
    save_data()
    print(f"Deleted expense: {removed_expense['date']} | {removed_expense['category']} | {removed_expense['description']} | {removed_expense['amount']}")
    print("Expense deleted successfully!\n\n")


# VIEW ALL DETAILS
def five():
    if not expenses:
        print("No expenses recorded.")
    else:
        total_amount = sum(expense['amount'] for expense in expenses)
        print("Date\t\tCategory\tDescription\tAmount")
        for expense in expenses:
            print(f"{expense['date']}, {expense['category']}, {expense['description']}, {expense['amount']}")

        print(f"Total Amount: {total_amount}")


# EXIT
def six():
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
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. View all details")
    print("6. Exit\n")

    choice = int(input("Enter your choice (1-6): "))
    if choice == 6:
        six()
        break
    elif choice < 1 or choice > 6:
        print("Invalid choice ")
    elif choice == 1:
        one()
    elif choice == 2:
        two()
    elif choice == 3:
        three()
    elif choice == 4:
        four()
    elif choice == 5:
        five()
    else:
        print("Invalid choice")


print("Thank you for using the Expense Tracker!")

