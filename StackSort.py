from IdentityPerm import identityp

def stacksort(p):
    stack = [p[0]]  # Immediately initalizes a stack and pushes first element of p
    n = len(p)
    s = []  # Output
    for i in range(n-1):  # Iterate over the 2nd through nth elements of p
        while stack != [] and p[i + 1] > stack[-1]:  # While nonempty and input > top of stack:
            s.append(stack.pop())                       # Pop the top of the stack
        stack.append(p[i+1])                         # Once the stack is empty or input < top, push input
    while stack:  # Clear the rest of the stack once last element is pushed
        s.append(stack.pop())
    return s

def stacksortFull(p):
    e = identityp(len(p))
    steps = [p]
    p0 = p
    while p0 != e:
        p0 = stacksort(p0)
        steps.append(p0)
    return steps

p = [4,2,6,1,5,3,7]
print(stacksortFull(p))