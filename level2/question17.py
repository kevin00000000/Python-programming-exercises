from functools import reduce
print(reduce(lambda x,y: x+y, [int(x.split(' ')[1]) if x.split(' ')[0]=="D" else 0-int(x.split(' ')[1]) for x in iter(input, "OK")]))
