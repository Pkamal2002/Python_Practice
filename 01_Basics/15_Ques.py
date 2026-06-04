# Write a program that accepts a sentence from the user and: a) Strips leading/trailing whitespace b)Replaces all spaces with underscores c) Checks whether the sentence starts with 'Hello' d) Splits it into a list of words and prints the list

user_string_input = input(" Enter a Sentence: ");

# a) Strips leading/trailing whitespace
stripped_string = user_string_input.strip();
print(" Stripped String is: ",stripped_string)

# b)Replaces all spaces with underscores
replaced_string = stripped_string.replace(" ","_")
print(" String with spaces replaced by underscores: ",replaced_string)
# c) Checks whether the sentence starts with 'Hello'
if stripped_string.startswith("Hello"):
    print(" String starts with Hello")
else:
    print(" String does not start with Hello")

# d) Splits it into a list of words and prints the list
word_list = stripped_string.split()
print(" List of Words in Sentence: ",word_list)