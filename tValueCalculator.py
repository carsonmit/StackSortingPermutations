from StackSort import stacksort


def identityp(n):  # Produces the identity of S_n
    if not isinstance(n, int):
        print("Enter an integer")  # Checks to make sure n is an integer
        return None
    e = []  # Initialize output
    for i in range(n):
        e.append(i+1)  # Adds the numbers 1-n in order to e and outputs e
    return e


def tval(p):  # Calculates the min no. of iterations t it takes a permutation p to reach e through the SSA
    count = 0  # Initialize output
    if p == identityp(len(p)):  # Checks if p is already the identity, if so t=0
        return count
    while p != identityp(len(p)):  # Else, SSA runs until e is reached and count = t is output
        count += 1
        p = stacksort(p)
    return count

