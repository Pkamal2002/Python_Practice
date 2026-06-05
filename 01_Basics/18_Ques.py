# Write a function is_palindrome(s) that returns True if the string s is a palindrome (reads the same forwards and backwards), ignoring case and spaces. Test with: 'racecar', 'A man a plan a canal Panama', 'hello'.

def is_palindrome(s):
    # Remove space
    s = s.replace(" ", "")
    # Convert into lowercase
    s = s.lower()

    rev_s = s[::-1];
    # if(s== rev_s):
    #     return True
    # else:
    #     return False
    return s == rev_s

print(is_palindrome('racecar'))
print(is_palindrome('A man a plan a canal Panama'))
print(is_palindrome('hello'))