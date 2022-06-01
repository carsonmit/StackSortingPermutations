from FundamentalParallelepipedEnumerator import *
from Ln1Permutations import *


# Attempt to make function bVectors more efficient for the simplexPoints function
def bVectorsSP(M):  # Replicates prior method, finds possible LPs the sum over lambda_iv_i can be (sum of lambdas is 1)
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
# Aha! Now with bVectorsSP instead of bVectors, n=4 is immediate, n=5 takes ~5sec, n=6 takes ~1min,...
def simplexPoints(vertices):
    M = sp.Matrix(vertices)
    M = M.T  # No lifting this time, just putting vecs as columns in a matrix
    bvecs = bVectorsSP(M)  # All possible LPs in the simplex
    lps = []
    sols = []
    for vec in bvecs:
        tup = liftAugMatrixRREF(M, vec)
        augMRREF = tup[0]  # Augments about each possible LP and puts in RREF
        numrows = (sp.shape(augMRREF))[0]
        counter = 0
        for i in range(numrows):
            if float(augMRREF.col(-1)[i]) < 0:  # We know system has a unique solution because points are LI
                counter += 1  # only need to check that lambda_i >= 0
        if counter == 0:
            sum = 0
            for i in range(numrows):  # Also checks the sum over lambda_i is 1
                sum += float(augMRREF.col(-1)[i])
            if sum == 1:
                lps.append(vec)  # If all checks pass, the int. point is in the FP and we add it to the lps vector
                sol = augMRREF.col(-1)  # Also adds the values of lambda that produce this LC in the sols vector
                sols.append(sol.T)
    return lps, sols


def LPsSP(vertices):  # Nicer way to visually output results of simplexPoints
    lps, sols = simplexPoints(vertices)
    if len(lps) != len(sols):
        return "Length error"
    num_lambdas = len(sols[0])
    print("The lattice points in the given simplex are:")
    for i in range(len(lps)):
        output = ""
        output += str(i+1) + ". " + str(lps[i]) + " from:  "
        for j in range(num_lambdas):
            output += "\u03BB_" + str(j+1) + " = " + str(sols[i][j]) + ",  "
        print(output)
    return None


n = 4
print(lPrimeFamily(n))
LPsSP(lPrimeFamily(n))
F = lPrimeFamily(n)
print("")
print(F)
LPsFP(F)