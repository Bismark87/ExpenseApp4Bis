

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


    def view_expenses(self):

        print("\nALL EXPENSES")
        if len(self.expenses) == 0:
        print("No expenses found.")
     else:
          for item in self.expenses:
                print("-----") print("Date:", item["date"])
                print("Category:", item["category"])
                print("Description:", item["description"])
                print("Amount: $", item["amount"])
                print("-----")

            total = expense_manager.get_total(self.expenses)
              print("Total Expenses: $", total)

     def filter_expenses(self):

        print("\nFILTER EXPENSES")
         start_date = input("Enter start date or press Enter to skip: ")
         end_date = input("Enter end date or press Enter to skip: ")
        category = input("Enter category or press Enter to skip: ")
          results = expense_filter.filter_expenses(
            self.expenses,
            start_date,
            end_date,
            category
        )
        print("\nFilter Results")
         if len(results) == 0:
          print("No matching expenses found.")
      else:
            for item in results:
              print("--------")
              print("Date:", item["date"])
              print("Category:", item["category"])
              print("Description:", item["description"])
            print("Amount: $", item["amount"])

     def save_expenses(self):
         print("\nSave Expenses")
           filename = input("Enter filename (expenses.json): ")
             file_handler.save_expenses(
            self.expenses, filename
        )
          print("Expenses saved successfully!")

     
     def open_expenses(self):
     print("\nOpen Expenses")
     filename = input("Enter filename (expenses.json): ")
      self.expenses = file_handler.open_expenses(filename)
        print("Expenses opened successfully!")     

        