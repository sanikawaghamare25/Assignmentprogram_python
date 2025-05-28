'''
3. First Non-Repeated Character
   - Write a function first_non_repeated(s) that returns the first non-repeated character in a string.
   - Example:  
     Input: "swiss"  
     Output: "w"
'''

#name=str(input("enter the string:"))
def first_non_repeated(s):
    for i in s:
        if s.count(i)==1:
            return i
    return 0

s=str(input("Enter the string:"))

print("first non repeat charecter:",first_non_repeated(s))



2)
#input="swiss"
input1=str(input("Enter the string:"))
char_order=[]
counts={}

for c in input1:
    if c in counts:
        counts[c]+=1


    else:
        counts[c]=1
        char_order.append(c)

for c in char_order:

    if counts[c]==1:
        print("first Non-Repeated charecter:",c)
        #break
