# Write a program that accepts two numbers from the user and prints the result of all arithmetic
# operators: +, -, *, /, //, %, **. Label each result clearly.

num1 =  int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))


# All Arithmetic printing
print(f"Sum {num1+num2}");
print(f"Difference {num1-num2}");
print(f"Multiply {num1*num2}")
print(f"Devide {num1/num2}");
print (f"Remainder {num1%num2}")
print(f"Power/Square {num1**num2}")
print (f"Floor {num1//num2}")

