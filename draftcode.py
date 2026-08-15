# EXPENSE TRACKER
import string 

import json
import os
from unicodedata import category

print("Welcome to the Expense Tracker!")
expenses = []
budgets = []

ExpenseTracker = "expenses.json"
BudgetTracker = "budgets.json"


# ADD EXPENSE
def one():
    date = input("Date (DD-MM-YYYY): ")
    Type = input("Type (Income/Expense): ")
    category = input("Category: ")
    description = input("Description: ")
    amount = float(input("Amount: "))
    Payment_Mode = input("Payment Mode: ")
    expense = {
        "date": date,
        "Type": Type,
        "category": category,
        "description": description,
        "amount": amount,
        "Payment Mode": Payment_Mode
    }
    expenses.append(expense)
    save_data()
    print("Expense added successfully!\n\n")


# VIEW EXPENSES
def two():
    if not expenses:
        print("No expenses recorded.\n\n")
    else:
        print("Date\t\t\tType\t\tCategory\tDescription\t\tAmount\t\tPayment Mode")
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense['date']}\t\t{expense['Type']}\t\t{expense['category']}\t\t{expense['description']}\t\t{expense['amount']}\t\t{expense['Payment Mode']}\n\n")

# UPDATE EXPENSE
def three():
    if not expenses:
        print("No expenses recorded.")
        return

    two()
    # CHATBOT GIVEN:
    # try:
    #     index = int(input("Enter the expense number to update: "))
    # except ValueError:
    #     print("Invalid expense number.")
    #     return

    # if index < 1 or index > len(expenses):
    #     print("Expense number out of range.")
    #     return

    index = int(input("Enter the expense number to update: "))
    if (index < 1 or index > len(expenses)):
        print("Expense number out of range.")
        return
        
    print("Enter the new expense details to replace the selected record.")
    date = input("New date (DD-MM-YYYY): ")
    Type = input("New Type (Income/Expense): ")
    category = input("New category: ")
    description = input("New description: ")
    amount = float(input("New amount: "))
    Payment_Mode = input("New Payment Mode: ")

    new_expense = {
        "date": date,
        "Type": Type,
        "category": category,
        "description": description,
        "amount": amount,
        "Payment Mode": Payment_Mode
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
    # try:
    #     index = int(input("Enter the expense number to delete: "))
    # except ValueError:
    #     print("Invalid expense number.")
    #     return

    # if index < 1 or index > len(expenses):
    #     print("Expense number out of range.")
    #     return

    index = int(input("Enter the expense number to delete: "))
    if (index < 1 or index > len(expenses)):
        print("Expense number out of range.")
        return
        
    removed_expense = expenses.pop(index - 1)
    save_data()
    print(f"Deleted expense data: {removed_expense['date']} | {removed_expense['Type']}  | {removed_expense['category']} | {removed_expense['description']} | {removed_expense['amount']} | {removed_expense['Payment Mode']}")
    print("Expense deleted successfully!\n\n")

# # SUMMARY REPORTS
def five():
    print("\n========== Monthly Summary Report =========\n")
    total_income = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Income").lower())
    total_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower())
    net_balance = total_income - total_expenses

    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Net Balance: {net_balance}")


    print("\n\n==========Category-wise Expense Report=========\n")
    salary_income = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Income").lower() and (expense['category']).lower() == ("Salary").lower())
    food_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Food").lower())
    travel_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("petrol").lower())
    bill_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("bills").lower())
    shopping_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Shopping").lower())
    groceries_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Groceries").lower())
    other_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Other").lower())


    print(f"Salary Income: Rs {salary_income}")
    print(f"Food Expenses: Rs {food_expenses}")
    print(f"Travel Expenses: Rs {travel_expenses}")
    print(f"Bill Expenses: Rs {bill_expenses}")
    print(f"Shopping Expenses: Rs {shopping_expenses}")
    print(f"Groceries Expenses: Rs {groceries_expenses}")
    print(f"Other Expenses: Rs {other_expenses}")    

    # BY COPILOT
    # categories = set(expense['category'] for expense in expenses)
    # for category in categories:
    #     category_income = sum(expense['amount'] for expense in expenses if expense['Type'] == "Income" and expense['category'] == category)
    #     category_expenses = sum(expense['amount'] for expense in expenses if expense['Type'] == "Expense" and expense['category'] == category)
    #     print(f"{category}:")
    #     print(f"  Total Income: {category_income}")
    #     print(f"  Total Expenses: {category_expenses}")
    #     print(f"  Net Balance: {category_income - category_expenses}")



# BUDGET MANAGER
def six():
    print("\n==========Budget Manager=========")
    food_budget = 0.0
    travel_budget = 0.0
    bill_budget = 0.0
    shopping_budget = 0.0
    groceries_budget = 0.0
    other_budget = 0.0

    monthly_budget = []

    if budgets:
        latest_budget = budgets[-1]
        food_budget = latest_budget.get("food budget", food_budget)
        travel_budget = latest_budget.get("travel budget", travel_budget)
        bill_budget = latest_budget.get("bills budget", bill_budget)
        shopping_budget = latest_budget.get("shopping budget", shopping_budget)
        groceries_budget = latest_budget.get("groceries budget", groceries_budget)
        other_budget = latest_budget.get("other budget", other_budget)


    sub_choice = True 
    while sub_choice != 0:
        
        print("\n Budget Managing Menu ")
        print("1. Set monthly Budget ")
        print("2. view current budget status ")
        print("3. update budget datails ")
        print("4. delate budget category ")
        print("0. EXIT budget menu ")
        sub_choice = int(input("\nEnter your choice (1-4): ")) 

        if sub_choice > 4 or sub_choice < 0:
            print("Invalis choice")            

        elif sub_choice == 1:
            print("\nSet Monthly Budget for each category:")
            food_budget = float(input("Food Budget: "))
            travel_budget = float(input("Travel Budget: "))
            bill_budget = float(input("Bill Budget: "))
            shopping_budget = float(input("Shopping Budget: "))
            groceries_budget = float(input("Groceries Budget: "))
            other_budget = float(input("Other Budget: "))

            monthly_budget = {
                "food budget": food_budget,
                "travel budget": travel_budget,
                "bills budget": bill_budget,
                "shopping budget": shopping_budget,
                "groceries budget": groceries_budget,
                "other budget": other_budget
            }

            # budgets.append(monthly_budget)
            # with open(budgets.json,"w") as file:
            #     json.writelines(monthly_budget)
            save_budget_data()
            print("Budget set successfully!")
            # break

        elif sub_choice == 2:
            salary_income = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Income").lower() and (expense['category']).lower() == ("Salary").lower())
            food_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Food").lower())
            travel_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("petrol").lower())
            bill_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("bills").lower())
            shopping_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Shopping").lower())
            groceries_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Groceries").lower())
            other_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Other").lower())
            
            print("\n==========Current Budget=========")
            print(f"Food Budget [ Rs {food_budget} ] : {food_expenses} ")
            print(f"Travel Budget [Rs {travel_budget} ] : {travel_expenses}")
            print(f"Bill Budget [Rs {bill_budget} : {bill_expenses}")
            print(f"Shopping Budget [ Rs {shopping_budget} ] : {shopping_expenses} ")
            print(f"Groceries Budget [Rs {groceries_budget} ] : {groceries_expenses}")
            print(f"Other Budget [Rs {other_budget} ] : {other_expenses}")
            # break

        elif sub_choice == 3:
            print("========== Update Budget Category =========")
            category_to_update = input("Enter the category to update budget (Food/Travel/Bill/Shopping/Groceries/Other): ")
            new_budget = float(input(f"Enter the new budget for {category_to_update}: "))
            if category_to_update.lower() == "food":
                food_budget = new_budget
            elif category_to_update.lower() == "travel":
                travel_budget = new_budget
            elif category_to_update.lower() == "bill":
                bill_budget = new_budget
            elif category_to_update.lower() == "shopping":
                shopping_budget = new_budget
            elif category_to_update.lower() == "groceries":
                groceries_budget = new_budget
            elif category_to_update.lower() == "other":
                other_budget = new_budget
            else:
                print("Invalid category.")
                continue

            monthly_budget = {
                "food budget": food_budget,
                "travel budget": travel_budget,
                "bills budget": bill_budget,
                "shopping budget": shopping_budget,
                "groceries budget": groceries_budget,
                "other budget": other_budget
            }
            if budgets:
                budgets[-1] = monthly_budget
            else:
                budgets.append(monthly_budget)
            save_budget_data()
            print(f"{category_to_update} budget updated successfully!")
            # break

        elif sub_choice == 4:
            category_to_delete = input("Enter the category to delete budget (Food/Travel/Bill/Shopping/Groceries/Other): ")
            if category_to_delete.lower() == "food":
                monthly_budget.pop(food_budget)
                # food_budget = None
            elif category_to_delete.lower() == "travel":
                travel_budget = None
            elif category_to_delete.lower() == "bill":
                bill_budget = None
            elif category_to_delete.lower() == "shopping":
                shopping_budget = None
            elif category_to_delete.lower() == "groceries":
                groceries_budget = None
            elif category_to_delete.lower() == "other":
                other_budget = None
            else:
                print("Invalid category.")
                continue

            monthly_budget = {
                "food budget": food_budget,
                "travel budget": travel_budget,
                "bills budget": bill_budget,
                "shopping budget": shopping_budget,
                "groceries budget": groceries_budget,
                "other budget": other_budget
            }
            if budgets:
                budgets[-1] = monthly_budget
            else:
                budgets.append(monthly_budget)
            save_budget_data()
            print(f"{category_to_delete} budget deleted successfully!")
                # break



# ALTRNATIVE BUDGET MANAGER CODE
    # print("Set Monthly Budget for each category:")
    # food_budget = float(input("Food Budget: "))
    # travel_budget = float(input("Travel Budget: "))
    # bill_budget = float(input("Bill Budget: "))
    # shopping_budget = float(input("Shopping Budget: "))
    # groceries_budget = float(input("Groceries Budget: "))
    # other_budget = float(input("Other Budget: "))

    # Budget alert:" spending above budget limit!".format(category)

    # print("1. Set Budget")
    # print("2. View Budget")
    # print("3. Update Budget")
    # # print("4. Delete Budget")
    # sub_choice = int(input("Enter your choice (1-4): "))
    # # if sub_choice < 0 or sub_choice > 4:
    #     print("Invalid choice. Please enter a valid option.")
    # elif sub_choice == 0:
    #     print("Exiting Budget Manager.")
    #     break
    # elif sub_choice == 1:
    #     print("Set Monthly Budget for each category:")
    #     food_budget = float(input("Food Budget: "))
    #     travel_budget = float(input("Travel Budget: "))
    #     bill_budget = float(input("Bill Budget: "))
    #     shopping_budget = float(input("Shopping Budget: "))
    #     groceries_budget = float(input("Groceries Budget: "))
    #     other_budget = float(input("Other Budget: "))
    #     print("Budget set successfully!") 

    # elif sub_choice == 2:
    #     food_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Food").lower())}")
            
    #     print(f"Food Budget Rs {food_budget} : {food_expenses}")

    # elif sub_choice == 3:
    #     new_budget = float(input("Enter the new budget for the category: "))
    #     print("Set Monthly Budget for each category:")
    #     new_foodbudget = float(input("New Food Budget: "))
    #     new_travelbudget = float(input("New Travel Budget: "))
    #     new_billbudget = float(input("New Bill Budget: "))
    #     new_shoppingbudget = float(input("New Shopping Budget: "))
    #     new_groceriesbudget = float(input("New Groceries Budget: "))
    #     new_otherbudget = float(input("New Other Budget: "))

    #     food_budget = new_foodbudget
    #     travel_budget = new_travelbudget
    #     bill_budget = new_billbudget
    #     shopping_budget = new_shoppingbudget
    #     groceries_budget = new_groceriesbudget
    #     other_budget = new_otherbudget
                

    


# # VISUALIZE DATA
# def Seven():


# VIEW ALL DETAILS
def eight():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\n=============== View all data Details ============== \n")
        print("Date\t\t\tType\t\tCategory\tDescription\t\tAmount\t\tPayment Mode")
        for expense in expenses:
            print(f"{expense['date']}\t\t{expense['Type']}\t\t{expense['category']}\t\t{expense['description']}\t\t{expense['amount']}\t\t\t\t\t{expense['Payment Mode']}")

        total_amount = sum(expense['amount'] for expense in expenses)
        total_income = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Income").lower())
        total_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower())
        net_balance = total_income - total_expenses
        
        print(f"\nTotal Transaction Amount: {total_amount}")
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Net Balance: {net_balance}\n\n")
        
# DELETE ALL DETAILS
def nine():
    if not expenses:
        print("No expenses recorded.")
        return

    confirmation = input("Are you sure you want to delete all expense records? (yes/no): ")
    if confirmation.lower() == "yes":
        expenses.clear()
        save_data()
        print("All expense records deleted successfully!\n\n")

        removed_expense = expenses.clear()
        save_data()
        print(f"Deleted expense data: {removed_expense['date']} | {removed_expense['Type']}  | {removed_expense['category']} | {removed_expense['description']} | {removed_expense['amount']} | {removed_expense['Payment Mode']}")

    else:
        print("Deletion canceled.\n\n")
   

# EXIT
def ten():
    save_data()
    print("Exiting..")


# Load data
if os.path.exists(ExpenseTracker):
    with open(ExpenseTracker, "r") as file:
        expenses = json.load(file)
else:
    expenses = []

if os.path.exists(BudgetTracker):
    with open(BudgetTracker, "r") as file:
        budgets = json.load(file)
else:
    budgets = []


def save_data():
    with open(ExpenseTracker, "w") as file:
        json.dump(expenses, file, indent=4)


def save_budget_data():
    with open(BudgetTracker, "w") as file:
        json.dump(budgets, file, indent=4)


while True:
    print("\n\n-------Menu-------")
    print("1. Add Expense")
    print("2. View Transactions")
    print("3. Update Transaction")
    print("4. Delete transaction")
    print("5. Summary Reports")
    print("6. Budget Manager")
    print("7. Visualize Data")
    print("8. View all details")
    print("9. Delete all details")
    print("10. Exit\n")

    choice = int(input("Enter your choice (1-10): "))
    if choice == 10:
        ten()
        break
    elif choice < 1 or choice > 10:
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
    elif choice == 6:
        six()
    elif choice == 7:
        Seven()
    elif choice == 8:
        eight()
    elif choice == 9:
        nine()
    else:
        print("Invalid choice")


print("Thank you for using the Expense Tracker!")

