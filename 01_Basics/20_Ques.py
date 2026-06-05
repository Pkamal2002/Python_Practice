# Write a program that proves strings are immutable by catching the TypeError when you attempt to modify a character. Then build a new string that is the original with the first character replaced. Compare memory addresses with id() before and after.

s = "raddit"

try:
    s[0] = 'b'  # This will raise an error
except TypeError as e:
    print(e)  # Output: 'str' object does not support item assignment
# Build a new string that is the original with the first character replaced
new_s = "R"+s[1:];
print(new_s)  # Output: "Raddit"
print(id(s))  # Memory address of the original string

print(id(new_s))  # Memory address of the new string
