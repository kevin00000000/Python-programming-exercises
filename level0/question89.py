print([x for (i,x) in enumerate([12,24,35,70,88,120,155]) if i!=0 and i!=4 and i!=5])
print([x for (i,x) in enumerate([12,24,35,70,88,120,155]) if i not in (0,4,5)])