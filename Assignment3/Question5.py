# Sample list of temperatures in Celsius
celsius_temperatures = [0, 10, 20, 30, 40, 100]

# Lambda function for conversion
fahrenheit_temperatures = list(map(lambda c: c * 9/5 + 32, celsius_temperatures))

# Print results
print("Celsius:", celsius_temperatures)
print("Fahrenheit:", fahrenheit_temperatures)