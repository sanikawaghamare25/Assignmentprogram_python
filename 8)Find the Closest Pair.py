'''
8. Find the Closest Pair
- Write a function find_closest_pair(numbers, target) that finds two
numbers in a list whose sum is closest to a target value.
- Example:
Input: numbers=[1, 3, 5, 8], target=10
Output: (3, 8)
'''
def find_closest_pair(numbers, target):
numbers.sort()
left=0
right=len(numbers)-1
closest_pair=None

closest_diff=float('inf')
while left< right:
current_sum=numbers[left]+numbers[right]
current_diff=abs(target-current_sum)
if current_diff<closest_diff:
closest_diff=current_diff
closest_pair=(numbers[left],numbers[right])
if current_sum<target:
left+=1
elif current_sum>target:
right-=1
return closest_pair
numbers=[1,3,5,8]
print("Numbers:",numbers)
target=10
print("Target:",target)
output=find_closest_pair(numbers,target)
print("sum is closest to pair:",output)
