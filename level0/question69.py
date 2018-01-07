n = int(input('Input a int: '))
def generator(n):
    for x in range(0, n+1):
        if x%5==0 and x%7==0:
            yield x
print(','.join([str(x) for x in generator(n)]))