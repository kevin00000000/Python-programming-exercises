row, column = [int(i) for i in input("Input two digits for i and j separated by comma: ").split(',')]
print("row:{0:d}    column:{1:d}".format(row, column))
result = []
temp = []
for i in range(0, row):
    temp = []
    for j in range(0, column):
        temp.append(i*j)
    result.append(temp)
    

print(result)