# Define custom exception
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass


# Function to check if a number is positive
def check_positive(number):
    """
    Checks if the number is positive.

    Parameters:
    number (int or float): The number to check.

    Raises:
    NegativeNumberError: If the number is negative.
    """
    if number < 0:
        raise NegativeNumberError("Error: Negative numbers are not allowed.")
    else:
        print(f"{number} is a positive number.")


# Demonstrate usage with try-except
try:
    num = float(input("Enter a number: "))
    check_positive(num)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a valid number.")