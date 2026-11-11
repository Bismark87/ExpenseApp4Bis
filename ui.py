

import expense  import expense_manager
import expensefilter  import file
import csv


class ExpenseUI:

    def __init__(self):

        self.expenses = []



    def add_expense(self):

        print("\nADD EXPENSE")

        date = input("Enter date (YYYY-MM-DD): ")

        category = input("Enter category: ")

        description = input("Enter description: ")

        amount = float(input("Enter amount: "))

        new_expense = expense.create_expense(
            date, category, description, amount
        )

        expense_manager.add_expense(
            self.expenses, new_expense
        )

        print("Expense added successfully!")