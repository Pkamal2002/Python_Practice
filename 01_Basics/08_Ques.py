# Write a program that accepts a floating-point temperature in Celsius from the user and converts it to
# Fahrenheit (F = C * 9/5 + 32). Display the result rounded to 2 decimal places. Also display the
# integer part using int() and the ceiling using math.ceil()

import math

temp = float(input("Enter temperature in Celsius: "))

fahrenheit = (temp * 9/5) + 32

print(f"Fahrenheit: {fahrenheit:.2f}")
print(f"Integer Part: {int(fahrenheit)}")
print(f"Ceiling Value: {math.ceil(fahrenheit)}")

