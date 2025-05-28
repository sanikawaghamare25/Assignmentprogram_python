'''
4. Check for Palindrome
- Write a function is_palindrome(s) that checks if a string is a palindrome.
- Extend it to ignore case and non-alphanumeric characters.
- Example:
Input: "A man, a plan, a canal, Panama"
Output: True
'''
import re
def is_palindrome(s):
string1=re.sub(r'[^a-zA-Z-9]','',s).lower()

return string1 == string1[::-1]

input_string="A man, a plan, a canal, Panama"

output=is_palindrome(input_string)
print(output)
