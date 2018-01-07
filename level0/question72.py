def BinarySearch(x, l, start, end):
    if(end < start):
        return None
    else:
        if x < l[int((start+end)/2)]:
            return BinarySearch(x, l, start, int((start+end)/2)-1)
        elif x>l[int((start+end)/2)]:
            return BinarySearch(x, l, int((start+end)/2)+1, end)
        else: return int((start+end)/2)

def Search(x, l):
    list.sort(l)
    return BinarySearch(x, l, 0, len(l)-1)

l = [17,2,7,9,11,222,5]
print('Index of 11 is {0:d}'.format(Search(11, l)))
print('Index of 9 is {0:d}'.format(Search(9, l)))
print(Search(100, l))