



def filter_expenses(expenses, start_date, end_date, category):

    results = []

    for expense in expenses:

        date_ok = True
        category_ok = True

        if start_date != "":
            if expense["date"] < start_date:
                date_ok = False

        if end_date != "":
            if expense["date"] > end_date:
                date_ok = False

        if category != "":
            if expense["category"].lower() != category.lower():
                category_ok = False

        if date_ok and category_ok:

            results.append(expense)

    return results
