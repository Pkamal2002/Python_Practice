# Write a Python program that tries to use a keyword (e.g. 'for', 'if', 'class') as a variable name and
# observe the error. Then fix it by choosing a valid variable name. Print all Python keywords using the
# 'keyword' module.


import keyword

# Using a keyword as a variable name (this will cause an error)
# for = 10 

for_value = 10
print("The value of for_value is:", for_value)

# Print all Python keywords
print("Python Keywords:", keyword.kwlist)

#Length of all python keywords

print("Python keyboard Count:", len(keyword.kwlist))
