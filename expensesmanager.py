import os

def add_expense(expenses):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    expenses.append({"category": category, "amount": amount})
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nExpenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['category']}: ${expense['amount']:.2f}")
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total: ${total:.2f}")

def save_expenses(expenses, filename="expenses.txt"):
    with open(filename, "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")
    print("Expenses saved to file!")

def load_expenses(filename="expenses.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [
            {"category": line.split(",")[0], "amount": float(line.split(",")[1])}
            for line in file.readlines()
        ]

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save and Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            save_expenses(expenses)
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
