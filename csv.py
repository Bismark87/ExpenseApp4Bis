


import csv


def expense(expenses, filename):

    file = open(filename, "w", newline="")

    writer = csv.writer(file)

    writer.writerow(["Date","Category","Description","Amount"
    ])

    for expense in expenses:

        writer.writerow([
            expense["date"],
            expense["category"],
            expense["description"],
            expense["amount"]
        ])

    file.close()