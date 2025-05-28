'''
10. Word Frequency Counter
- Write a function word_frequency(s) that takes a string and returns the
frequency of each word in a dictionary.
- Ignore case and punctuation.

- Example:
Input: "To be or not to be"
Output: {'to': 2, 'be': 2, 'or': 1, 'not': 1}
'''

import string
def word_frequency(s):
s=s.translate(str.maketrans("","",string.punctuation)).lower()
words=s.split()
frequency={}
for word in words:
frequency[word]=frequency.get(word,0)+1
return frequency #{word:frequency}
input_text="To be or not to be"
print("String:",input_text)
output=word_frequency(input_text)
print(output)
