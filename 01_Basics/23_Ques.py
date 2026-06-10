# # Write a program to compress a string using run-length encoding. 'aabbbccddddee' should become'a2b3c2d4e2'. If a character appears only once, just write the character without '1'. Your output for'abcd' should be 'abcd'.

string = "aabbbccddddee"

enc = ""
st = string[0]
count = 0

for ch in string:
    if ch == st:
        count += 1
    else:
        enc += st if count == 1 else st + str(count)
        st = ch
        count = 1

enc += st if count == 1 else st + str(count)

print(enc)