n = int(input('input a int: '))
def generator(n):
    for x in range(0,n+1):
        if x%2==0:
            yield x
print(','.join([str(x) for x in generator(n)]))