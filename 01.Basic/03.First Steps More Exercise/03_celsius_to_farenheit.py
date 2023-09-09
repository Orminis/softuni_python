#Convert temperature reading from Celsius degrees to Fahrenheit degrees.
# Format the result to second number after the decimal point
degrees_c = float(input())

fahrenheit = (9 / 5 * degrees_c) + 32
print(f"{fahrenheit:.2f}")