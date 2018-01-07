def genNum(digit, times):
    result = digit
    if times>=1 and digit>0 and digit<10:
        for i in range(1, times):
            result = result*10+digit
    return result

def sum(digit, num):
    result = 0
    for x in range(1, num+1):
        result += genNum(digit, x)
    return result
print(sum(1, 3))

def genNumWithStr(digit, times):
    template = '{:d}'
    value = [digit]
    if times>=1 and digit>0 and digit<10:
        for i in range(1, times):
            template += '{:d}'
            value.append(digit)
    return int(template.format(*value))

def sumWithStr(digit, num):
    result = 0
    for x in range(1, num+1):
        result += genNumWithStr(digit, x)
    return result
print(sumWithStr(1, 3))
