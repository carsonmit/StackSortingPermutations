from PermutationTools.AllPermutationsLexicographic import allPerms
from PermutationTools.IdentityPermutation import identityp
from StackSort import stacksort


def tValue(p):  # Calculates the minimum # of iterations t it takes a permutation p to reach e through the SSA
    t = 0  # Initialize output
    if p == identityp(len(p)):  # Checks if p is already the identity, if so t=0
        return t
    while p != identityp(len(p)):  # Else, SSA runs until e is reached and count = t is output
        t += 1
        p = stacksort(p)
    return t


def tValues(n):  # Finds the num of SSA iterations to e for EVERY permutation 1 to n in lexicographic order
    perms = allPerms(n)
    tvalues = []
    for perm in perms:
        tvalues.append(tValue(perm))
    return tvalues