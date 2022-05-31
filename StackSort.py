from PermutationTools.AllPermutationsLexicographic import allPerms
from PermutationTools.IdentityPermutation import identityp


def stacksort(p):  # Stack sorting algorithm on a given permutation p (as a list)
    stack = [p[0]]  # Immediately initializes a stack and pushes first element of p
    n = len(p)
    s = []  # Initializes output of the stack
    for i in range(n - 1):  # Iterate over the 2nd through nth elements of p
        while stack != [] and p[i + 1] > stack[-1]:  # While nonempty and input > top of stack:
            s.append(stack.pop())  # Pop the top of the stack
        stack.append(p[i + 1])  # Once the stack is empty or input < top, push input
    while stack:  # Clear the rest of the stack once last element is pushed
        s.append(stack.pop())
    return s


def stacksortFull(p):  # Repeats the stacksort function until the identity is reached and outputs all iterations
    e = identityp(len(p))
    steps = [p]  # Initializes output, input permutation is first bc it is the 0th iteration
    p0 = p  # Temp variable so p is not overwritten in steps
    while p0 != e:
        p0 = stacksort(p0)
        steps.append(p0)
    return steps


def stacksortFullLex(n):  # Performs stacksortFull on EVERY permutation from 1 to n and prints results (in lex order)
    perms = allPerms(n)
    for perm in perms:
        print(stacksortFull(perm))