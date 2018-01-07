listOriginal = [1,2,3,4,5,6,7,8,9,10]
result = list(map(lambda x: x**2, filter(lambda y: y%2==0, listOriginal)))
print(result)

print([x**2 for x in [y for y in listOriginal if y%2==0]])
print([x+y+z for x in range(1, 3) for y in range(11, 13) for z in range(101, 103)])