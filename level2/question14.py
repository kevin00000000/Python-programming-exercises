listChar = [x for x in input('Input a sentence: ')]

upperNum = 0
lowerNum = 0
for c in listChar:
    if str.isupper(c):
        upperNum = upperNum + 1
    if str.islower(c):
        lowerNum = lowerNum + 1
print('LETTERS {0:d}\nDIGITS {1:d}'.format(upperNum, lowerNum))
