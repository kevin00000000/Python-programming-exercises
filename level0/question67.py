def Fibonacci(n):
    if n<=0: return 0
    elif n==1: return 1
    else: return Fibonacci(n-1)+Fibonacci(n-2)
n = 7
print(','.join([str(Fibonacci(x)) for x in range(0, n+1)]))