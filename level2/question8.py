items = [x for x in input("input a seq of words seperated by comma: ").split(',')]
items.sort()
print(','.join(items))