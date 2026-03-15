import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Division by zero"
    else:
        return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}



def calculator():
    print(art.logo)
    number_1 = float(input("Enter a number: "))

    flag = True
    while flag:
        for symbol in operations:
            print(symbol)
        operation = input("Enter operation: ")
        number2 = float(input("Enter another number: "))
        result = operations[operation](number_1, number2)
        print(f"{number_1} {operation} {number2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            number_1 = result
        else:
            flag = False
    calculator()

calculator()