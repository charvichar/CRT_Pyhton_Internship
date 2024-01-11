"""
Import modules
1. Json: Save and load tasks in Json
2. Tabulate: Represent in tabular form
"""

import json
from tabulate import tabulate

#File to save the budget report
budgetTracker = "budget_tracker.json"

#Checking if the file exists
def load():
    try:
        with open(budgetTracker, "r" ) as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"income": 0, "expenses" : []}
    return data

#Adding data to file
def save(data):
    with open(budgetTracker, "w") as file:
        json.dump(data, file)

#Defining what the app has to offer
def menu():
    print("\n ====Budget Tracker💸====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. View Expense Analysis")
    print("5. Exit")

#Adding income
def addIncome(data):
    amount = float(input("Enter your income: "))
    data["income"] += amount
    print(f"Your income of Rs.{amount} has been added successfully!")

#Adding expenses
def addExpense(data):
    category = input("Enter the category of your expense: ")
    amount = float(input("Enter the amount of expense: "))
    data["expenses"].append({"category": category, "amount": amount})

#Reviewing budget
def viewBudget(data):
    remaining_budget = data["income"] - sum(item["amount"] for item in data["expenses"])
    print("Your budget is as follows: ")
    print(f"\n Income: Rs.{data['income']}")
    print(f"\n Total Expenses: Rs.{sum(item['amount'] for item in data['expenses'])}")
    print(f"\n Remaining budget: Rs.{remaining_budget}")

#Categorically analysing the expenses in tabular form
def expenseAnalysis(data):
    expensesCategory = {}
    for item in data["expenses"]:
        category = item["category"]
        amount = item["amount"]
        expensesCategory[category] = expensesCategory.get(category, 0) + amount
    print("\n Expense Analysis: ")
    print(tabulate(expensesCategory.items(), headers = ["Category", "Total"], tablefmt = "fancy_grid"))
    print()

#Main function with switch case
def main():
    data = load()

    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            addIncome(data)
        elif choice == "2":
            addExpense(data)
        elif choice == "3":
            viewBudget(data)
        elif choice == "4":
            expenseAnalysis(data)
        elif choice == "5":
            save(data)
            print("Your budget data has been saved successfully! See you soon!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5!")

if __name__ == "__main__":
    main()

