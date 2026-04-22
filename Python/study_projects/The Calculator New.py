#Using dictionary method
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1-n2

def divide(n1, n2):
    return n1/n2

def multiply(n1, n2):
    return n1*n2

calculator_dict = {"+": add,
                   "-": sub,
                   "*": multiply,
                   "/": divide,
                   }

def calculator():
    calculate = True
    print(r"""
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """)
    num1 = int(input("What is the first number?\n"))
    while calculate:
        for operator in calculator_dict:
            print(operator)
        operator = input(f"Which operation would you like to perform.\n")
        num2 = int(input("What is the second number?\n"))
        total = calculator_dict[operator](num1, num2)
        print(f"The result is:{num1} {operator} {num2} = {total}")
        calculate_check = str(input("Would you wanna calculate more? yes or no: \n"))
        if calculate_check == "yes":
                num1 = total
        else:
                calculate = False
                print(f"The result is:{num1} {operator} {num2} = {total}")
                calculator()

calculator()