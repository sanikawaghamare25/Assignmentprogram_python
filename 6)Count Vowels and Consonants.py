'''
6. Count Vowels and Consonants
- Create a function count_vowels_consonants(s) that counts the number of
vowels and consonants in a string.
- Example:
Input: "Hello World"
Output: {'vowels': 3, 'consonants': 7}'''



#s= str(input("Enter string:"))
def count_vowels_consonants(s):
vowels="aeiouAEIOU"
vowels_count=0
consonants_count=0

for char in s:
if char.isalpha():
if char in vowels:
vowels_count+=1
else:
consonants_count+=1
return{'vowels':vowels_count,'consonants':consonants_count}
input_string="Hello World"
print("Input String:",input_string)

output=count_vowels_consonants(input_string)
print(output)
