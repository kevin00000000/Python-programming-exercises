result = [str(int(x)**2) for x in input("Input a seq of number separated by comma:").split(',') if int(x)%2!=0]
print(','.join(result))