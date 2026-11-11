
import expense
import expensemanager
import expensefilter
import file
import csv


class ExpenseUI:

    def __init__(self):
        self.expenses = []

    def run(self):

        while True:

            print("\n--- Expense Tracker ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Filter Expenses")
            print("4. Save Expenses")
            print("5. Open Expenses")
            print("6. Export to CSV")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == "1":

                date = input("Date (YYYY-MM-DD): ")
                category = input("Category: ")
                description = input("Description: ")
                amount = float(input("Amount: "))

                new_expense = expense.create_expense(
                    date, category, description, amount
                )

                expensemanager.add_expense(
                    self.expenses, new_expense
                )

                print("Expense added!")

            elif choice == "2":

                for item in self.expenses:
                    print(item)

                print("Total: $", expensemanager.get_total(self.expenses))

            elif choice == "3":

                start = input("Start date: ")
                end = input("End date: ")
                category = input("Category: ")

                results = expensefilter.filter_expenses(
                    self.expenses, start, end, category
                )

                for item in results:
                    print(item)

            elif choice == "4":

                filename = input("JSON filename: ")
                file.save_expenses(self.expenses, filename)
                print("Expenses saved!")

            elif choice == "5":

                filename = input("JSON filename: ")
                self.expenses = file.open_expenses(filename)
                print("Expenses opened!")

            elif choice == "6":

                filename = input("CSV filename: ")
                file.export_expenses(self.expenses, filename)
                print("CSV exported!")

            elif choice == "7":

                print("Goodbye!")
                break

            else:

                print("Invalid choice!")