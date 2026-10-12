def add_numbers(num1, num2):
 return num1 + num2
def subtract_numbers(num1, num2):
 return num1 - num2
def multiply_numbers(num1, num2):
 return num1 * num2
def divide_numbers(num1, num2):
 if num2 == 0:
  return "Error! No division by zero."
 return num1 / num2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = (input("Choose an operation (+, -, *, /):"))
if operation== "+":
    result = add_numbers(num1, num2)
elif operation == "-":
    result = subtract_numbers(num1, num2)
elif operation == "*":
    result = multiply_numbers(num1, num2)
elif operation == "/":
    result = divide_numbers(num1, num2)
else:
    print("Not a valid operation! Choose either +, -, *, or /")
print(result)
