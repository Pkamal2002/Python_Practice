# Write a function that accepts a sentence and returns it with every word reversed but the word order preserved. For example: 'Hello World' → 'olleH dlroW' Do not use any external library.

def sentence_reserved(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
       
    reversed_sentence = " ".join(reversed_words)
    print(reversed_sentence)

sentence_reserved("Hello World")
