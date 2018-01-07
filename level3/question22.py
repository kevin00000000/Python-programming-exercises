listWords = [x for x in input('Input a seq of words: ').split(' ')]
dictWords = {}
for x in listWords:
    dictWords[x] = dictWords.get(x, 0)+1
listDst = list(dictWords.keys())
listDst.sort()
for x in listDst:
    print('{0:s} {1:d}'.format(x, dictWords[x]))
