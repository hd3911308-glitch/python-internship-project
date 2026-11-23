
from datetime import date

from expense import (
    FoodExpense,
    TravelExpense,
    GeneralExpense
)

from expense_manager import ExpenseManager


manager = ExpenseManager()


def create_new_expense():

    try:
        amount = float(input("Enter expense amount: Rs. "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        print("\nSelect Expense Type:")
        print("1. Food")
        print("2. Travel")
        print("3. General")

        choice = input("Enter your choice: ")

        category = input("Enter category: ")
        description = input("Enter description: ")

        if not category.strip() or not description.strip():
            print("Category and description cannot be empty.")
            return

        if choice == "1":
            expense = FoodExpense(amount, category, description)

        elif choice == "2":
            expense = TravelExpense(amount, category, description)

        elif choice == "3":
            expense = GeneralExpense(amount, category, description)

        else:
            print("Invalid expense type.")
            return

        manager.add_expense(expense)
        print("\nExpense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def update_existing_expense():

    manager.view_expenses()

    try:
        index = int(input("\nEnter expense number to update: ")) - 1

        amount = float(input("Enter new amount: Rs. "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter new category: ")
        description = input("Enter new description: ")

        if not category.strip() or not description.strip():
            print("Category and description cannot be empty.")
            return

        if manager.update_expense(index, amount, category, description):
            print("\nExpense updated successfully!")
        else:
            print("\nInvalid expense number.")

    except ValueError:
        print("Please enter valid numeric values.")


def delete_existing_expense():

    manager.view_expenses()

    try:
        index = int(input("\nEnter expense number to delete: ")) - 1

        if manager.delete_expense(index):
            print("\nExpense deleted successfully!")
        else:
            print("\nInvalid expense number.")

    except ValueError:
        print("Please enter a valid expense number.")


def show_monthly_summary():

    month = input("Enter month (YYYY-MM): ")

    try:
        date.fromisoformat(month + "-01")
        manager.monthly_summary(month)

    except ValueError:
        print("Invalid month format. Use YYYY-MM.")


def main():

    while True:

        print("\n========== PERSONAL EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. View Total Expenses")
        print("7. Monthly Expense Summary")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_new_expense()

        elif choice == "2":
            manager.view_expenses()

        elif choice == "3":
            category = input("Enter category to search: ")
            manager.search_expenses(category)

        elif choice == "4":
            update_existing_expense()

        elif choice == "5":
            delete_existing_expense()

        elif choice == "6":
            total = manager.calculate_total()
            print(f"\nTotal Expenses: Rs. {total:.2f}")

        elif choice == "7":
            show_monthly_summary()

        elif choice == "8":
            print("\nThank you for using Personal Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
