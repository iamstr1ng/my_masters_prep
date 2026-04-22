#Calculate using if /else
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1-n2

def divide(n1, n2):
    return n1/n2

def multiply(n1, n2):
    return n1*n2

calculate = True
total = 0
num1 = int(input("What is the first number?\n"))

while calculate:
    operator = input("Which operation would you like to perform. \n")
    num2 = int(input("What is the second number?\n"))
    if operator == "+":
        total = add(num1,num2)
    elif operator == "-":
        total = sub(num1, num2)
    elif operator == "*":
        total = multiply(num1, num2)
    elif operator == "/":
        total = divide(num1, num2)
    else:
        print("Incorrect operator choose again")
    print(f"The result is: {total}")
    calculate_check = str(input("Would you wanna calculate more? yes or no: \n"))
    if calculate_check == "yes":
            calculate = True
            num1 = total
    else:
            calculate = False
            print(f"The result is: {total}")
