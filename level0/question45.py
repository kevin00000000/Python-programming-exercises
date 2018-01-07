listOriginal = [1,2,3,4,5,6,7,8,9,10]
result = list(map(lambda x: x**2, listOriginal))
print(result)

print([x**2 for x in [1,2,3,4,5,6,7,8,9,10]])