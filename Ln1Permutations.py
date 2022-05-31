from PermutationTools.AllPermutationsLexicographic import allPerms
from StackSort import stacksortFull


def lPrime(n):  # Given n, produces the perm L'n1
    lp = []
    for i in range(n - 1):
        lp.append(i + 2)  # Starts by adding the numbers 2,3,...,n
    lp.append(1)  # Adds 1 to the end
    return lp


def lPrimeFamily(n):  # Produces a set of n perms, the L'n1 family, F(L'n1)
    lp = lPrime(n)
    return stacksortFull(lp)


def allLn1(n):  # Produces a set of (n-2)! perms, all perms of the form Ln1
    perms = allPerms(n)  # All permutations of 1,...,n in lexicographic order
    Ln1 = []
    for perm in perms:
        if perm[-2] == n and perm[-1] == 1:
            Ln1.append(perm)  # Checks each perm to see if it ends with n1, if so is added to output
    return Ln1
