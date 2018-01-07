listOrig = [x for x in input("Input a seq of words seperated by whitesapce: ").split(' ')]
listDst = sorted(list(set(listOrig)))
print(' '.join(listDst))