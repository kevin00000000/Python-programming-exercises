def divisible7(n):
    for x in range(0,n):
        if x%7==0:
            yield x

print([x for x in divisible7(1000)])