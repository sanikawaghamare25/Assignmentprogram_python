7. String Compression
- Implement a function compress_string(s) that compresses a string by
replacing sequences of repeated characters with the character followed by
the count.
- Example:
Input: "aaabbccccd"
Output: "a3b2c4d1"
'''

def compress_string(s):
if not s:
return""
compressed=[]
count=1
for i in range(1,len(s)):
if s[i]==s[i-1]:
count+=1
else:
compressed.append(f"{s[i-1]}{count}")

count=1

compressed.append(f"{s[i-1]}{count}")
return''.join(compressed)
input_string="aaabbbcccd"
print("Input String:",input_string)
output=compress_string(input_string)
print("string Compression:",output)
