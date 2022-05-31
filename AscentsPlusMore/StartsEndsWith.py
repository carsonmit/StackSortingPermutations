from PermutationTools.AllPermutationsLexicographic import allPerms


def startsWith(p):
    return p[0]


def endsWith(p):
    return p[-1]


def startsWithLex(n):  # Finds the first number of EVERY permutation 1 to n in lexicographic order
    perms = allPerms(n)
    starts_with = []
    for perm in perms:
        starts_with.append(perm[0])
    return starts_with


def endsWithLex(n):  # Finds the last number of EVERY permutation 1 to n in lexicographic order
    perms = allPerms(n)
    ends_with = []
    for perm in perms:
        ends_with.append(perm[-1])
    return ends_with