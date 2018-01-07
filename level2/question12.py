result = []
for x in range(1000, 3001):
    div = x
    mod = 0
    while div!=0:
        mod = div%10
        if mod%2!=0:
            break
        div = div//10
    if div == 0:
        result.append(str(x))

print(','.join(result))