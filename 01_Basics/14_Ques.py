# Given the string s = 'PythonProgramming', write slicing expressions to extract: a) 'Python' b) 'Programming' c) 'nohtyP' (reversed) d) Every second character

s = 'PythonProgramming';
# a) 'Python'
print(s[0:6])

# b) 'Programming'
print(s[6:])

# c) 'nohtyP' (reversed)
print(s[5::-1])

# d) Every second character
# print(s[::2])

for i in range(0, len(s), 2):
    print(s[i], end='')

