"""
Main script for the calculator module. 
This asks the user for two numbers and an operation and then performs it.
"""

import calculator # imports the calculator created

# Ask user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation with error handling
try:
    if operation == "+":
        result = calculator.add(num1, num2)
    elif operation == "-":
        result = calculator.subtract(num1, num2)
    elif operation == "*":
        result = calculator.multiply(num1, num2)
    elif operation == "/":
        result = calculator.divide(num1, num2)
    else:
        print("Invalid operation")
        result = None

        
    if result is not None:
         print(f"The result is: {result}")

        
        
except ZeroDivisionError as e:
        print (f"Error: {e}")






