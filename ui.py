
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
            print("\n1. Add Expensee")
            print("2. view expenses")
            print("3. filter expenses")
            print("4. save JSON")
            print("5. open JSON")
            print("6. export CSV")
            print("7. exit")

            choice = input("Choose: ")

            if choice == "1":
                date = input("Date: ")
                category = input("Category: ")
                description = input("Description: ")
                amount = float(input("Amount: "))
                new_expense = expense.create_expense(
                    date, category, description, amount)
                expensemanager.add_expense(
                    self.expenses, new_expense)

            elif choice == "2":
                for item in self.expenses:
                    print(item)

            elif choice == "3":
                start = input("Start date: ")
                end = input("End date: ")
                category = input("Category: ")
                results = expensefilter.filter_expenses(
                    self.expenses, start, end, category)
                for item in results:
                    print(item)

            elif choice == "4":
                filename = input("Filename: ")
                file.save_expenses(self.expenses, filename)

            elif choice == "5":
                filename = input("Filename: ")
                self.expenses = file.open_expenses(filename)

            elif choice == "6":
                filename = input("Filename: ")
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["Date", "Category", "Description", "Amount"])
                    for item in self.expenses:
                        writer.writerow([item.date, item.category, item.description, item.amount])

            elif choice == "7":
                print("Goodbye!")
                break
        else:
                print("Invalid choice!")
