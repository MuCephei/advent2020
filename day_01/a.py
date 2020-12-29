def get_expenses(target):
    expenses = {}

    with open('input.txt', 'r') as file:
        for line in file.readlines():
            expense = int(line)
            inverse = target - expense
            if inverse in expenses:
                return inverse * expense
            expenses[expense] = True


print(get_expenses(2020))