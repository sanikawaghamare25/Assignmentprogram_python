
'''
4. Check for Palindrome
   - Write a function is_palindrome(s) that checks if a string is a palindrome.
   - Extend it to ignore case and non-alphanumeric characters.
   - Example:  
     Input: "A man, a plan, a canal, Panama"  
     Output: True
'''

input1="A man, a plan, a canal, Panama"
def is_palindrome(input1):
    lower=input1.lower()
    str1=""
    for input1 in lower:

        if input1.isalpha():# isalpha-->removed the space in list of the words
            str1=str1+input1
    reverse=str1[::-1]

    if str1==reverse:
        return True
    else:
        return False
print("String is palindrome:",is_palindrome(input1))

2)
import re
def is_palindrome(s):
    string1=re.sub(r'[^a-zA-Z-9]','',s).lower()

    return string1 == string1[::-1]

input_string="A man, a plan, a canal, Panama"
output=is_palindrome(input_string)
print(output)


