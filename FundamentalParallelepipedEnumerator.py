import sympy as sp
import itertools as it
from Ln1Permutations import *


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


# Major efficiency issues -- n=3 is immediate, after that not so much... (it only works with Ln1 fams right now)
def latticePointsFP(vertices):  # Finds lattice points in the fund. parallelepiped of P w given vertices
    M = liftedMatrix(vertices)  # Lifts vertices to generators of the FP using liftedMatrix function
    bvecs = bVectors(M)  # Finds all possible int. points that lin. combs. of the generators w 0<=lambda<1 can be
    lps = []
    sols = []
    for vec in bvecs:
        tup = liftAugMatrixRREF(M, vec)
        augMRREF = tup[0]  # For each possible int. point, augments it about FP generators to see if is solvable
        numcols = (sp.shape(augMRREF))[1]
        counter = 0
        for i in range(numcols - 1):
            if augMRREF.row(-1)[i] != 0:  # Checks if bottom row is all 0s
                counter += 1
        if counter == 0 and augMRREF.col(-1)[-1] != 0:  # If bottom right value is non0 in row of 0s,
            continue  # then system is inconsistent and skip
        numrows = (sp.shape(augMRREF))[0]
        counter2 = 0
        for i in range(numrows):  # Checks that each of lambda_i is >=0 and <1
            if float(augMRREF.col(-1)[i]) >= 1 or float(augMRREF.col(-1)[i]) < 0:
                counter2 += 1
        if counter2 == 0:  # If all checks pass, the int. point is in the FP and we add it to the lps vector
            lps.append(vec)
            sol = augMRREF.col(-1)  # Also outputs the values of the lambda that produce this lin. comb.
            sols.append(sol.T)
    return lps, sols


n = 4
F = lPrimeFamily(n)
print(F)
print(latticePointsFP(F))
