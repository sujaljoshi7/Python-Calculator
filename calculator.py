from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    continue_calculation = True
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    while continue_calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_operation = (
            input("Do you want to continue calculation with previous answer? Type 'y' to continue and 'n' to exit "))
        if continue_operation != "n":
            num1 = answer
        else:
            continue_calculation = False
            calculator()


calculator()
