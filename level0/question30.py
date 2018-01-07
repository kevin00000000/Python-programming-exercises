def printMaxLen(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 > len2:
        print(str1)
    elif len1 < len2:
        print(str2)
    else:
        print(str1)
        print(str2)
printMaxLen('abc', 'a')
printMaxLen('c', 'cba')
printMaxLen('abc', 'ABC')