#iterator
input = 8
result = 1
for i in range(1,input+1):
    result = result * i
print(result)

#recursion
def fact(i):
    if i<0:
        return 0
    if i==0:
        return 1
    else:
        return i*fact(i-1)
print(fact(8))