import math
C = 50
H = 30
DSeq = list(input("Input a seq of D: ").split(','))

Result = []
for D in DSeq:
    Result.append(str(int(round(math.sqrt(2*C*float(D)/H)))))
print(','.join(Result))