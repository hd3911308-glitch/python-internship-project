
import json
import os

from expense import create_expense


class ExpenseManager:

    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("Invalid expense data.")

            self.expenses = [create_expense(item) for item in data]

        except (json.JSONDecodeError, OSError, KeyError,
                TypeError, ValueError) as error:
            print("Error loading expenses:", error)
            self.expenses = []

    def save_expenses(self):
        try:
            with open(self.filename, "w") as file:
                data = [expense.to_dict() for expense in self.expenses]
                json.dump(data, file, indent=4)

        except OSError as error:
            print("Error saving expenses:", error)

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses found.")
            return

        print("\n--- All Expenses ---")

        for index, expense in enumerate(self.expenses, start=1):
            print(f"\nExpense Number: {index}")
            print("Date:", expense.expense_date)
            print("Amount:", expense.amount)
            print("Category:", expense.category)
            print("Description:", expense.description)
            print("Type:", expense.get_expense_type())

    def search_expenses(self, category):
        found = False

        print("\n--- Search Results ---")

        for index, expense in enumerate(self.expenses, start=1):
            if expense.category.lower() == category.lower():
                print(
                    f"{index}. {expense.category} - "
                    f"Rs. {expense.amount} - {expense.description}"
                )
                found = True

        if not found:
            print("No matching expenses found.")

    def update_expense(self, index, amount, category, description):
        if 0 <= index < len(self.expenses):

            old_expense = self.expenses[index]

            new_expense = type(old_expense)(
                amount,
                category,
                description,
                old_expense.expense_date
            )

            self.expenses[index] = new_expense
            self.save_expenses()
            return True

        return False

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            self.save_expenses()
            return True

        return False

    def calculate_total(self):
        return sum(expense.amount for expense in self.expenses)

    def get_monthly_expenses(self, month):
        return [
            expense for expense in self.expenses
            if expense.expense_date[:7] == month
        ]

    def monthly_summary(self, month):
        monthly_expenses = self.get_monthly_expenses(month)

        if not monthly_expenses:
            print("\nNo expenses found for", month)
            return

        total = sum(expense.amount for expense in monthly_expenses)

        category_totals = {}

        for expense in monthly_expenses:
            category = expense.category
            category_totals[category] = (
                category_totals.get(category, 0) + expense.amount
            )

        print("\n--- Monthly Expense Summary ---")
        print("Month:", month)
        print("Number of Expenses:", len(monthly_expenses))
        print(f"Total Expenses: Rs. {total:.2f}")

        print("\nCategory-wise Expenses:")

        for category, amount in category_totals.items():
            print(f"{category}: Rs. {amount:.2f}")
