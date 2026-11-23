# Personal Expense Tracker

## 1. Project Overview
The Personal Expense Tracker is a console-based Python application designed to record, manage, and monitor daily expenses. It allows users to add, view, search, update, and delete expense records. It also provides total expense calculations and monthly expense summaries.

## 2. Objectives
- To develop a practical application using Python.
- To understand and implement Object-Oriented Programming.
- To manage expense records efficiently.
- To store data permanently using JSON.
- To generate monthly expense summaries.

## 3. Technologies Used
- Python 3
- Visual Studio Code
- JSON
- Git and GitHub

## 4. Main Features
1. Add Expense
2. View Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Calculate Total Expenses
7. Monthly Expense Summary
8. JSON-based Data Storage

## 5. Project Structure
- `main.py` – Handles the main menu and user interaction.
- `expense.py` – Defines expense classes and their types.
- `expense_manager.py` – Handles expense operations and data management.
- `expenses.json` – Stores expense records.
- `README.md` – Project documentation.

## 6. OOP Concepts Used
- **Abstraction:** Uses an abstract Expense class.
- **Encapsulation:** Uses private attributes and properties.
- **Inheritance:** FoodExpense, TravelExpense, and GeneralExpense inherit from Expense.
- **Polymorphism:** Different expense classes implement the same method, `get_expense_type()`.

## 7. How to Run
1. Install Python 3.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

   `python3 main.py`

5. Select an option from the displayed menu.

## 8. Result
The application successfully manages expense records, stores data using JSON, and generates monthly expense summaries.

## 9. Conclusion
This project provided practical experience in Python programming, Object-Oriented Programming, exception handling, JSON file handling, and project development.
