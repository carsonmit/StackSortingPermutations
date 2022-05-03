from StackSort import stacksortFull
import sympy as sp
import itertools as it
from AllPermutationsLexicographic import allperms


def lprime(n):  # Given n, produces the perm L'n1
    lp = []
    for i in range(n - 1):
        lp.append(i + 2)  # Starts by adding the numbers 2,3,...,n
    lp.append(1)  # Adds 1 to the end
    return lp


def lprimefamily(n):  # Produces a set of n perms, the L'n1 family, F(L'n1)
    lp = lprime(n)
    return stacksortFull(lp)


def allLn1(n):  # Produces a set of (n-2)! perms, all perms of the form Ln1
    perms = allperms(n)  # All permutations of 1,...,n in lexicographic order
    Ln1 = []
    for perm in perms:
        if perm[-2] == n and perm[-1] == 1:
            Ln1.append(perm)  # Checks each perm to see if it ends with n1, if so is added to output
    return Ln1


def appendOneAll(vectors):  # Given a set of vectors, appends 1 to the end of each of them (for lifting polytopes)
    for vector in vectors:
        vector.append(1)
    return vectors


def liftedMatrix(vectors):  # Creates the lifted matrix needed for RREF in the latticePointsFP function
    liftedM = appendOneAll(vectors)  # Adds one to all row vectors
    M = sp.Matrix(liftedM)  # Turns it into a matrix
    M = M.T  # Make the lifted vectors the columns instead of the rows to solve system x_1w_1 + ... = Mx = b
    return M


def bVectors(liftedM):  # Replicates method we do by hand, finds all possible LPs the sum over lambda_iw_i can be
    maxvalues = []
    for i in range(sp.shape(liftedM)[0]):  # Assumes each lambda is 1 to obtain an upper bound for each coordinate
        sum = 0
        for j in range(sp.shape(liftedM)[1]):
            sum += liftedM.row(i)[j]
        maxvalues.append(sum)
    possvalues = []
    for val in maxvalues:  # Takes value x from maxvalues and outputs list [0,1,...,x-1], all possibilities for coord.
        values = [num for num in range(val)]
        possvalues.append(values)
    bvecs = list(it.product(*possvalues))  # Takes the Cartesian prod of possvals to find all possible LPs
    return bvecs


def liftAugMatrixRREF(liftedM, b):  # Takes a matrix M and vector b and puts the augmented (M|b) in RREF
    newM = sp.Matrix(liftedM)
    newb = sp.Matrix(b)
    dimM = sp.shape(newM)  # Returns tuple with (numrows, numcols)
    colsM = dimM[1]  # Fetches numcols
    newM = newM.col_insert(colsM + 1, newb)  # Appends b to last column
    rrefM = newM.rref()
    return rrefM


def dilateP(vertices, factor):  # Takes vertices v_1,...,v_n and factor c to return cv_1,...,cv_n
    for vertex in vertices:
        for i in range(len(vertex)):
            vertex[i] = vertex[i] * factor
    return vertices


# Major efficiency issues -- n=3 is immediate, n=4 takes ~1min, n=5 takes ~2hours,...
def latticePointsFP(vertices):  # Finds lattice points in the fund. parallelepiped of P w given vertices
    M = liftedMatrix(vertices)  # Lifts vertices to generators of the FP using liftedMatrix function
    bvecs = bVectors(M)  # Finds all possible int. points that lin. combs. of the generators w 0<= lambda < 1 can be
    lps = []
    sols = []
    for vec in bvecs:
        tuple = liftAugMatrixRREF(M, vec)
        augMRREF = tuple[0]  # For each possible int. point, augments it about FP generators to see if is solvable
        numcols = (sp.shape(augMRREF))[1]
        counter = 0
        for i in range(numcols - 1):
            if augMRREF.row(-1)[i] != 0:  # Checks if bottom row is all 0s
                counter += 1
        if counter == 0 and augMRREF.col(-1)[-1] != 0:  # If bottom right value is non0 in row of 0s,
            continue                                    # then system is inconsistent and skip
        numrows = (sp.shape(augMRREF))[0]
        counter2 = 0
        for i in range(numrows):  # Checks that each of lambda_i is >= 0 and < 1
            if float(augMRREF.col(-1)[i]) >= 1 or float(augMRREF.col(-1)[i]) < 0:
                counter2 += 1
        if counter2 == 0:  # If all checks pass, the int. point is in the FP and we add it to the lps vector
            lps.append(vec)
            sol = augMRREF.col(-1)  # Also outputs the values of the lambda that produce this lin. comb.
            sols.append(sol.T)
    return lps, sols


# Attempt to make function bVectors more efficient for the simplexPoints function
def SPbVectors(M):  # Replicates prior method, finds possible LPs the sum over lambda_iv_i can be (sum of lambdas is 1)
    maxvalues = []
    for i in range(sp.shape(M)[0]):  # Finds the max over each coordinate to find the upper bound for that coordinate
        max = 0
        for j in range(sp.shape(M)[1]):
            if M.row(i)[j] > max:
                max = M.row(i)[j]
        maxvalues.append(max)
    possvalues = []
    for val in maxvalues:  # Takes value x from maxvalues and outputs list [0,1,...,x], all possibilities for coord.
        values = [num for num in range(val + 1)]
        possvalues.append(values)
    bvecs = list(it.product(*possvalues))  # Takes the Cartesian prod of possvals to find all possible LPs
    return bvecs


# Efficiency issues -- n=3 is immediate, n=4 takes ~15secs, n=5 takes ~15mins,...
# Aha! Now with SPbVectors instead of bVectors, n=4 is immediate, n=5 takes ~5sec, n=6 takes ~1min,...
def simplexPoints(vertices):
    M = sp.Matrix(vertices)
    M = M.T  # No lifting this time, just putting vecs as columns in a matrix
    bvecs = SPbVectors(M)  # All possible LPs in the simplex
    lps = []
    sols = []
    for vec in bvecs:
        tuple = liftAugMatrixRREF(M, vec)
        augMRREF = tuple[0]  # Augments about each possible LP and puts in RREF
        numrows = (sp.shape(augMRREF))[0]
        counter = 0
        for i in range(numrows):
            if float(augMRREF.col(-1)[i]) < 0:  # We know system has a unique solution because points are LI
                counter += 1                    # only need to check that lambda_i >= 0
        if counter == 0:
            sum = 0
            for i in range(numrows):            # Also checks the sum over lambda_i is 1
                sum += float(augMRREF.col(-1)[i])
            if sum == 1:
                lps.append(vec)  # If all checks pass, the int. point is in the FP and we add it to the lps vector
                sol = augMRREF.col(-1)  # Also adds the values of lambda that produce this LC in the sols vector
                sols.append(sol.T)
    return lps, sols


n = 4
F = lprimefamily(n)
G = stacksortFull([3, 2, 4, 1])
# P = dilateP(F,3)
# print(P)

print(F)
print(latticePointsFP(F))
#print(simplexPoints(F))

# print(latticePointsFP([[1,2,3],[2,2,2]]))
