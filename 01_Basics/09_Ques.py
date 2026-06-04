# Explain the difference between '==' and 'is' by writing a short program using small integers, large
# integers, and strings. Show at least one case where '==' returns True but 'is' returns False. Add
# comments explaining Python's object interning.

arr1 = [1, 2]
arr2 = [1, 2]

print("Lists:")
print(arr1 == arr2)
print(arr1 is arr2)

str1 = "abc"
str2 = "abc"

print("\nStrings:")
print(str1 == str2)
print(str1 is str2)

a = 10
b = 10

print("\nSmall Integers:")
print(a == b)
print(a is b)