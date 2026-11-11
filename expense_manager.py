



def add_expense(expenses, expense):

    expenses.append(expense)


def get_total(expenses):

    total = 0

    for expense in expenses:

        total = total + expense["amount"]

    return total
