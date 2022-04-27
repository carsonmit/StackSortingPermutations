from IdentityPerm import identityp
from NumAscents import numAscents


def allperms(n):  # Enumerates all perms of 1-n in lexicographic order
    p = identityp(n)  # First is the identity
    list = [identityp(n)]  # Initialize output
    while numAscents(p) != 0:  # If numAscents = 0, then p = n(n-1)...321 and we are at the last one
        index1 = 0  # Step 1: find the largest i (index1) s.t. p[i]<p[i+1] (the last ascent)
        for i in range(n - 1):  # Every time an ascent is found, index1 is updated to the new largest such i
            if p[i] < p[i + 1]:
                index1 = i
        index2 = index1 + 1  # Step 2: Find the largest j s.t j>i and p[j]>p[i]. Clearly, j >= i + 1
        j = index2  # Temp for iteration
        while j < n:  # Updates index2 every time a new largest j is found
            if p[j] > p[index1]:
                index2 = j
            j += 1
        nextp = p  # Temp for step 3
        x = p[index1]  # Step 3: swap p[i] and p[j]
        nextp[index1] = nextp[index2]
        nextp[index2] = x
        array = [nextp[i] for i in range(index1 + 1, n)]  # Temp for step 4
        array = array[::-1]  # Step 4: reverse p[i+1],...,p[n-1] and output new p
        for i in range(index1 + 1, n):
            nextp[i] = array[i - index1 - 1]
        temp = []  # Stuff to avoid stupid issues with lists
        temp += nextp
        list.append(temp)
    return list
