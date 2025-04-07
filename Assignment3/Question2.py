def calculate_average(*args):
    """
    Calculate the average of a variable number of numerical arguments.

    Parameters:
        *args (float or int): A variable number of numerical arguments.

    Returns:
        float: The average of the provided numbers. Returns None if no numbers are provided.
    """
    if not args:
        return None  # Return None if no numbers are provided

    return sum(args) / len(args)


# Input screen for numbers
numbers = input("Enter numbers separated by spaces: ")
numbers = [float(num) for num in numbers.split()]

# Calculate and print the average
average = calculate_average(*numbers)
print("Average:", average)