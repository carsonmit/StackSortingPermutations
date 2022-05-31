def identityp(n):  # Produces the identity of S_n
    if not isinstance(n, int):
        print("Enter an integer")  # Checks to make sure n is an integer
        return None
    e = []  # Initialize output
    for i in range(n):
        e.append(i+1)  # Adds the numbers 1-n in order to e and outputs e
    return e