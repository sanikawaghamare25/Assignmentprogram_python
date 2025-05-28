'''
5. Fibonacci Sequence
   - Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence.
   - Ensure the function works efficiently using memoization.
'''

def fibonacci(n,memo={}):
    #global n,memo
    if n<=0:
        return[]
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]


    if n not in memo:
        seq=fibonacci(n - 1,memo)
        seq.append(seq[-1] + seq[-2])
        memo[n]= seq
    return memo[n]
    
        
n=int(input("Enter the number:"))
print(f"First {n} Fibonacci numbers: {fibonacci(n)}")


2)

def fib(k,fib_memo={}):
    
    if k in fib_memo:
        return fib_memo[k]
    
    if k==1:
        value=1

    elif k==2:
        value=1
    
    elif k>2:
        value=fib(k-1)+fib(k-2)

    fib_memo[k]=value
    return value

for k in range(1,7):
    print(fib(k))


