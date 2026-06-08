# Given a list of students with names and marks, print a neatly aligned table using f-strings with width specifiers. Column widths: Name=20, Marks=6 (right-aligned). students = [('Priya', 88), ('Rahul', 92), ('Sneha', 76)]

students = [('Priya', 88), ('Rahul', 92), ('Sneha', 76)]

print(f"{'Name':<20} | {'Marks':>6}")
print("-" * 30)
for name, marks in students:
    print(f"{name:<20} | {marks:>6}")
