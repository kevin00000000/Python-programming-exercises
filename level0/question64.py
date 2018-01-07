def recusion(n):
    if n<=0:
        return 0
    if n==1:
        return 1/2
    else:
        return n/(n+1)+recusion(n-1)
def iterator(n):
    sum = 0
    for i in range(1,n+1):
        sum += ((i)/(i+1))
    return sum

print(recusion(5))
print(iterator(5))