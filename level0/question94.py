s = input('Input a sentense: ')
d = {}
for x in s:
    d[x] = d.get(x, 0)+1
    
print(d)
for k, v in d.items():
    print('{:s}, {:d}'.format(k, v))