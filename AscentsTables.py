from AllPermutationsLexicographic import allperms
from NumAscents import numAscents
from tValueCalculator import tval
import pandas as pd

def numAscentsLex(n):
    perms = allperms(n)
    list = []
    for perm in perms:
        list.append(numAscents(perm))
    return list

def startsWith(p):
    return p[0]

def startsWithLex(n):
    perms = allperms(n)
    list = []
    for perm in perms:
        list.append(perm[0])
    return list

def tvals(n):
    perms = allperms(n)
    list = []
    for perm in perms:
        list.append(tval(perm))
    return list

def tIndices(list,item):
    x=-1
    indices = []
    while True:
        try:
            index = list.index(item,x+1)
        except ValueError:
            break
        else:
            indices.append(index)
            x = index
    return indices

def ascentSSTable(n):
    ascents = numAscentsLex(n)
    tvalues = tvals(n)
    columns = []
    for i in range(n):
        indices = tIndices(ascents, i)
        newtvalues = []
        for index in indices:
            newtvalues.append(tvalues[index])
        column = []
        for j in range(n):
            count = 0
            for val in newtvalues:
                if val == j:
                    count += 1
            column.append(count)
        columns.append(column)
    table = pd.DataFrame(columns)
    table = table.transpose()
    return table

def startsWithSSTable(n):
    sw = startsWithLex(n)
    tvalues = tvals(n)
    columns = []
    for i in range(1,n+1):
        indices = tIndices(sw, i)
        newtvalues = []
        for index in indices:
            newtvalues.append(tvalues[index])
        column = []
        for j in range(n):
            count = 0
            for val in newtvalues:
                if val == j:
                    count += 1
            column.append(count)
        columns.append(column)
    labels = [i for i in range(1,n+1)]
    table = pd.DataFrame(columns)
    table = table.transpose()
    return table.rename(columns ={i:labels[i] for i in range(n)})


def endsWith(p):
    return p[-1]

def endsWithLex(n):
    perms = allperms(n)
    list = []
    for perm in perms:
        list.append(perm[-1])
    return list

def endsWithSSTable(n):
    ew = endsWithLex(n)
    tvalues = tvals(n)
    columns = []
    for i in range(1,n+1):
        indices = tIndices(ew, i)
        newtvalues = []
        for index in indices:
            newtvalues.append(tvalues[index])
        column = []
        for j in range(n):
            count = 0
            for val in newtvalues:
                if val == j:
                    count += 1
            column.append(count)
        columns.append(column)
    labels = [i for i in range(1,n+1)]
    table = pd.DataFrame(columns)
    table = table.transpose()
    return table.rename(columns ={i:labels[i] for i in range(n)})