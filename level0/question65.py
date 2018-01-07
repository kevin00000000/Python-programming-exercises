def recusion(n):
    if n<=0:
        return 0
    else:
        return recusion(n-1)+100
print(recusion(5))