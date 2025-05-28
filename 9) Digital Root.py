'''
9. Digital Root
- Create a function digital_root(n) that recursively calculates the digital root
of a number (the sum of its digits until the result is a single digit).
- Example:
Input: 942
Output: 6
'''
def digital_root(n):
if n<10:
return n
digit_sum=sum(int(digit)for digit in str(n))
return digital_root(digit_sum)
input_number=942
print("Number:",input_number)
output=digital_root(input_number)
print("Digital root of a number:",output)
