def get_expenses(target):
    expenses = {}
    double_expenses = {}

    with open('input.txt', 'r') as file:
        for line in file.readlines():
            expense = int(line)
            inverse = target - expense
            if inverse in double_expenses:
                return expense * double_expenses[inverse][0] * double_expenses[inverse][1]
            add_expense(expense, expenses, double_expenses, inverse)


def add_expense(expense, expenses, double_expenses, inverse):
    for e in expenses:
        if inverse < expense:
            continue
        summation = e + expense
        if summation in double_expenses:
            continue
        double_expenses[summation] = [e, expense]

    expenses[expense] = True


print(get_expenses(2020))