from StackSort import stacksort
from IdentityPerm import identityp

def tval(p):  # Calculates the min no. of iterations t it takes a permutation p to reach e through the SSA
    count = 0  # Initialize output
    if p == identityp(len(p)):  # Checks if p is already the identity, if so t=0
        return count
    while p != identityp(len(p)):  # Else, SSA runs until e is reached and count = t is output
        count += 1
        p = stacksort(p)
    return count