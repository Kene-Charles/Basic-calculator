# Building a calculator using Python
operator = input("Enter on of this operators (+ - * /): ")
num1 = float(input("Enter a number:"))
num2 = float(input("Enter a number:"))

if operator == "+":
    Result = num1 + num2
    print(Result)
elif operator == "-":
    Result = num1 - num2
    print(Result)
elif operator == "*":
    Result = num1 * num2
    print(Result)
elif operator == "/":
    Result = num1 / num2
    print(round(Result ,2))
else:
    print(f"{operator} is an invalid operator")

