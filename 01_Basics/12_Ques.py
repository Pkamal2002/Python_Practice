# Write a program that demonstrates mutability in Python. Show that: (a) lists are mutable (change an
# element in place), (b) strings are immutable (try to change a character and catch the error), and (c)
# tuples are immutable. Discuss in comments why immutability matters in function arguments and dictionary keys


# a) lists are mutable
my_list = [1, 2, 3]
my_list[0] = 99
print(my_list)  # Output: [99, 2, 3]

# b) strings are immutable
my_string = "Hello"
try:
    my_string[0] = 'h'  # This will raise an error
except TypeError as e:
    print(e)  # Output: 'str' object does not support item assignment

#
# c) tuples are immutable
my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 99  # This will raise an error
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment

# Discuss in comments why immutability matters in function arguments and dictionary keys
# Immutability matters in function arguments because if you pass a mutable object (like a list) to a function, the function can modify that object, which can lead to unintended side effects. For example:
def modify_list(lst):
    lst.append(4)
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
# In contrast, if you pass an immutable object (like a string), the function cannot modify it, which can help prevent bugs and make the code easier to understand.
# Immutability also matters for dictionary keys because only immutable objects can be used as keys in a dictionary. This is because the hash value of a key must remain constant throughout its lifetime, and mutable objects can change their hash value, which would lead to unpredictable behavior in the dictionary. For example:
my_dict = {}
my_dict[my_tuple] = "This is a tuple key"  # This works because tuples are immutable
try:
    my_dict[my_list] = "This is a list key"  # This will raise an error because lists are mutable
except TypeError as e:
    print(e)  # Output: unhashable type: 'list'


