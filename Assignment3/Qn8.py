import random

def generate_random_numbers(count=10, start=1, end=100):
    """Generates a list of random integers."""
    return [random.randint(start, end) for _ in range(count)]

def calculate_average(numbers):
    """Calculates and returns the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0  # Avoid division by zero

# Generate random numbers
random_numbers = generate_random_numbers()

# Calculate average
average = calculate_average(random_numbers)

# Print results
print("Generated Numbers:", random_numbers)
print("Average:", average)