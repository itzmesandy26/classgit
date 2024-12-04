try:
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))
    
    result = dividend / divisor
        
    print(f"The result of {dividend} divided by {divisor} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")

