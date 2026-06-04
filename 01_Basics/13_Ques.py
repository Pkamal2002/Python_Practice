# Write a program that takes a sentence as input and prints: a) The total number of characters
# (including spaces) b) The number of words c) The sentence in uppercase d) The sentence with the
# first letter of each word capitalised

input_Sentence = input(" Enter a Sentence: ");

# a) The total number of characters (including spaces)
print ("Total Number of Character in Sentence: ",len(input_Sentence));
# b) The number of words

words = input_Sentence.split();
print(" Number of Words in Sentence are:  ",len(words))

# c) The sentence in uppercase
print(" Sentence in Uppercase: ",input_Sentence.upper())

# d) The sentence with the first letter of each word capitalised
print(" Sentence with first letter of each word capitalised: ",input_Sentence.title())