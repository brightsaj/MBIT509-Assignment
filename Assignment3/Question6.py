def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")

# Get user input
try:
    num = float(input("Enter the numerator: "))
    denom = float(input("Enter the denominator: "))
    print("Result:", divide_numbers(num, denom))
except ValueError:
    print("Error: Please enter valid numeric values.")