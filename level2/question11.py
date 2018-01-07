listBin = [int(x, base=2) for x in input("Input a seq of comma separated 4 digit binary numbers: ").split(',')]
result = [str(bin(x))[2:] for x in listBin if x%5==0]
print(','.join(result))