listChar = [x for x in input('Input a sentence: ')]

letterNum = 0
digitNum = 0
for c in listChar:
    if str.isdigit(c):
        digitNum = digitNum + 1
    if str.isalpha(c):
        letterNum = letterNum + 1
print('LETTERS {0:d}\nDIGITS {1:d}'.format(letterNum, digitNum))
