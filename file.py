

import json


def save_expenses(expenses, filename):
     file = open(filename, "w")
     json.dump(expenses, file, indent=4)

     file.close()


def open_expenses(filename):
    file = open(filename, "r")
    expenses = json.load(file)
    file.close()

    return expenses
