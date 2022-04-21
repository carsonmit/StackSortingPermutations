def numAscents(p):  # Number of ascents in a given permutation p
    count = 0  # Initialize output
    n = len(p)
    for i in range(n-1):  # Checks each consecutive pair in p for an ascent, adds to the count if found
        if p[i] < p[i+1]:
            count += 1
    return count
