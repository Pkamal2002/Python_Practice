# Write a program to demonstrate Python's memory model. Create two lists a = [1,2,3] and b = a.
# Modify b[0] = 99 and print both a and b. Then repeat with b = a.copy() and explain the difference
# between a shallow copy and a reference assignment. Use id() to show whether variables point to
# the same object.

a = [1,2,3]
b = a

b[0] = 99;
print(a)
print(b)
print(id(a))
print(id(b))

# b = a.copy();
# b[0] = 99;
# print(a)
# print(b)
# print(id(a))
# print(id(b))

