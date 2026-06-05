# Write a program that takes a string and counts the frequency of each character (case-insensitive, ignoring spaces). Display results sorted alphabetically. Do NOT use Counter — use only basic string methods and a dictionary.

input_string = input(" Enter a String: ")
# Remove space
input_string = input_string.replace(" ", "")
# Convert into lowercase
input_string = input_string.lower()
char_freq = {}
for char in input_string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
# Sort the dictionary by key and display results
for char in sorted(char_freq.keys()):
    print(f"{char}: {char_freq[char]}")
