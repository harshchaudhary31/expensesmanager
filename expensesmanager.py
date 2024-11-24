import tkinter as tk
from tkinter import messagebox
import os

# Functions for expense management
def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    if not category or not amount:
        messagebox.showerror("Input Error", "Please fill in both fields.")
        return
    try:
        amount = float(amount)
        expenses.append({"category": category, "amount": amount})
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Expense added successfully!")
        update_expenses_list()
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")

def update_expenses_list():
    expense_list.delete(0, tk.END)
    total = 0
    for i, expense in enumerate(expenses, 1):
        expense_list.insert(tk.END, f"{i}. {expense['category']}: ${expense['amount']:.2f}")
        total += expense['amount']
    total_label.config(text=f"Total: ${total:.2f}")

def save_expenses(filename="expenses.txt"):
    with open(filename, "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']},{expense['amount']}\n")
    messagebox.showinfo("Saved", "Expenses saved to file!")

def load_expenses(filename="expenses.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [
            {"category": line.split(",")[0], "amount": float(line.split(",")[1])}
            for line in file.readlines()
        ]

# Initialize expenses
expenses = load_expenses()

# Create main window
window = tk.Tk()
window.title("Expense Tracker")
window.geometry("400x400")

# Input fields
tk.Label(window, text="Category:").pack(pady=5)
category_entry = tk.Entry(window, width=30)
category_entry.pack(pady=5)

tk.Label(window, text="Amount:").pack(pady=5)
amount_entry = tk.Entry(window, width=30)
amount_entry.pack(pady=5)

# Buttons
tk.Button(window, text="Add Expense", command=add_expense).pack(pady=10)
tk.Button(window, text="Save Expenses", command=lambda: save_expenses()).pack(pady=5)

# Expense list
tk.Label(window, text="Expenses:").pack(pady=10)
expense_list = tk.Listbox(window, width=50, height=10)
expense_list.pack(pady=5)

# Total label
total_label = tk.Label(window, text="Total: $0.00", font=("Arial", 12, "bold"))
total_label.pack(pady=10)

# Load initial data into the list
update_expenses_list()

# Run the main loop
window.mainloop()
