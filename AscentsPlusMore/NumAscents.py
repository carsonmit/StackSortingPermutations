from PermutationTools.AllPermutationsLexicographic import allPerms


def numAscents(p):  # Number of ascents in a given permutation p
    num_ascents = 0  # Initialize output
    n = len(p)
    for i in range(n-1):  # Checks each consecutive pair in p for an ascent, adds to the count if found
        if p[i] < p[i+1]:
            num_ascents += 1
    return num_ascents


def numAscentsLex(n):  # Finds the number of ascents in EVERY permutation 1 to n in lexicographic order
    perms = allPerms(n)
    num_ascents_list = []
    for perm in perms:
        num_ascents_list.append(numAscents(perm))
    return num_ascents_list
