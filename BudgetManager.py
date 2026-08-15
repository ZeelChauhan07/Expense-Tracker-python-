import json
import os

BudgetTracker = "budgets.json"
budgets = []


def load_budgets():
    """Load budgets from JSON file"""
    global budgets
    if os.path.exists(BudgetTracker):
        with open(BudgetTracker, "r") as file:
            budgets = json.load(file)
    else:
        budgets = []


def save_budget_data():
    """Save budgets to JSON file"""
    with open(BudgetTracker, "w") as file:
        json.dump(budgets, file, indent=4)


def set_monthly_budget():
    """Set monthly budget for each category"""
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

    budgets.append(monthly_budget)
    save_budget_data()
    print("Budget set successfully!")


def view_budget_status(expenses):
    """View current budget status against actual spending"""
    if not budgets:
        print("No budget set yet. Please set a budget first.")
        return

    latest_budget = budgets[-1]
    food_budget = latest_budget.get("food budget", 0.0)
    travel_budget = latest_budget.get("travel budget", 0.0)
    bill_budget = latest_budget.get("bills budget", 0.0)
    shopping_budget = latest_budget.get("shopping budget", 0.0)
    groceries_budget = latest_budget.get("groceries budget", 0.0)
    other_budget = latest_budget.get("other budget", 0.0)

    # Calculate actual expenses
    food_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Food").lower())
    travel_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("petrol").lower())
    bill_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("bills").lower())
    shopping_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Shopping").lower())
    groceries_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Groceries").lower())
    other_expenses = sum(expense['amount'] for expense in expenses if (expense['Type']).lower() == ("Expense").lower() and (expense['category']).lower() == ("Other").lower())

    print("\n==========Current Budget Status=========")
    print(f"Food Budget [ Rs {food_budget} ] : Spent Rs {food_expenses}")
    print(f"Travel Budget [ Rs {travel_budget} ] : Spent Rs {travel_expenses}")
    print(f"Bill Budget [ Rs {bill_budget} ] : Spent Rs {bill_expenses}")
    print(f"Shopping Budget [ Rs {shopping_budget} ] : Spent Rs {shopping_expenses}")
    print(f"Groceries Budget [ Rs {groceries_budget} ] : Spent Rs {groceries_expenses}")
    print(f"Other Budget [ Rs {other_budget} ] : Spent Rs {other_expenses}\n")


def update_budget_category():
    """Update budget for a specific category"""
    if not budgets:
        print("No budget set yet. Please set a budget first.")
        return

    print("========== Update Budget Category =========")
    category_to_update = input("Enter the category to update budget (Food/Travel/Bill/Shopping/Groceries/Other): ")
    new_budget = float(input(f"Enter the new budget for {category_to_update}: "))

    latest_budget = budgets[-1]
    
    if category_to_update.lower() == "food":
        latest_budget["food budget"] = new_budget
    elif category_to_update.lower() == "travel":
        latest_budget["travel budget"] = new_budget
    elif category_to_update.lower() == "bill":
        latest_budget["bills budget"] = new_budget
    elif category_to_update.lower() == "shopping":
        latest_budget["shopping budget"] = new_budget
    elif category_to_update.lower() == "groceries":
        latest_budget["groceries budget"] = new_budget
    elif category_to_update.lower() == "other":
        latest_budget["other budget"] = new_budget
    else:
        print("Invalid category.")
        return

    budgets[-1] = latest_budget
    save_budget_data()
    print(f"{category_to_update} budget updated successfully!")


def delete_budget_category():
    """Delete budget for a specific category"""
    if not budgets:
        print("No budget set yet. Please set a budget first.")
        return

    print("========== Delete Budget Category =========")
    category_to_delete = input("Enter the category to delete budget (Food/Travel/Bill/Shopping/Groceries/Other): ")

    latest_budget = budgets[-1]

    if category_to_delete.lower() == "food":
        latest_budget["food budget"] = 0.0
    elif category_to_delete.lower() == "travel":
        latest_budget["travel budget"] = 0.0
    elif category_to_delete.lower() == "bill":
        latest_budget["bills budget"] = 0.0
    elif category_to_delete.lower() == "shopping":
        latest_budget["shopping budget"] = 0.0
    elif category_to_delete.lower() == "groceries":
        latest_budget["groceries budget"] = 0.0
    elif category_to_delete.lower() == "other":
        latest_budget["other budget"] = 0.0
    else:
        print("Invalid category.")
        return

    budgets[-1] = latest_budget
    save_budget_data()
    print(f"{category_to_delete} budget deleted successfully!")


def manage_budget(expenses):
    """Main budget management menu"""
    print("\n==========Budget Manager=========")
    
    sub_choice = True
    while sub_choice != 0:
        print("\n Budget Managing Menu ")
        print("1. Set monthly Budget ")
        print("2. View current budget status ")
        print("3. Update budget details ")
        print("4. Delete budget category ")
        print("0. EXIT budget menu ")
        sub_choice = int(input("\nEnter your choice (1-4): "))

        if sub_choice > 4 or sub_choice < 0:
            print("Invalid choice")

        elif sub_choice == 1:
            set_monthly_budget()

        elif sub_choice == 2:
            view_budget_status(expenses)

        elif sub_choice == 3:
            update_budget_category()

        elif sub_choice == 4:
            delete_budget_category()

        elif sub_choice == 0:
            break

        else:
            print("Invalid choice")
