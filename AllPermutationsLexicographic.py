from tValueCalculator import identityp
from NumAscents import numAscents

def allperms(n):
    p = identityp(n)
    list = [identityp(n)]
    while numAscents(p) != 0:
        index1 = 0
        for i in range(n-1):
            if p[i] < p[i+1]:
                index1 = i
        index2 = index1 + 1
        j = index2
        while j < n:
            if p[j] > p[index1]:
                index2 = j
            j += 1
        nextp = p
        x = p[index1]
        nextp[index1] = nextp[index2]
        nextp[index2] = x
        array = [nextp[i] for i in range(index1+1, n)]
        array = array[::-1]
        for i in range(index1+1,n):
            nextp[i] = array[i - index1 - 1]
        empty = []
        empty += nextp
        list.append(empty)
    return list
