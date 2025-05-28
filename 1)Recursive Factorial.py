'''
1. Recursive Factorial
   - Write a function factorial(n) that calculates the factorial of a number recursively.
   - Test it with both small and large numbers to see if it handles recursion depth.

'''

small_number=int(input("Enter the small number:"))
large_number=int(input("Enter the large number:"))
def factorial(small_number):
    if small_number >= 1:
        
        return small_number* factorial(small_number - 1)

    else:
        
        return 1
print("factorial of small num is:",factorial(small_number))

def fact(large_number):
    

    if large_number >= 1:
    
        return large_number* fact(large_number - 1)

    else:
        return 1
print("factorial of large num is:",fact(large_number))

Output:




                 
