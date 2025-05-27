expression = input("Expression: ").strip()

# Remove spaces from the expression
expression = expression.replace(" ", "")

# Find the operator in the expression
if "+" in expression:
    num1, num2 = expression.split("+")
    operator = "+"
elif "-" in expression:
    num1, num2 = expression.split("-")
    operator = "-"
elif "*" in expression:
    num1, num2 = expression.split("*")
    operator = "*"
elif "/" in expression:
    num1, num2 = expression.split("/")
    operator = "/"
else:
    print("Invalid expression.")
    exit()

# Convert num1 and num2 to integers
num1 = float(num1)
num2 = float(num2)

# Perform the operation based on the operator
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero.")
