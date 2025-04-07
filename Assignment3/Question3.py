while True:
    try:
        number = float(input("Enter a number: "))  # Accepts integers and decimals
        print(f"You entered: {number}")
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Invalid input. Please enter a valid number.")