from MiscellaneousTools.FindIndices import findIndices
from NumAscents import *
from StartsEndsWith import *
from tValueCalculator import *
import pandas as pd


def ascentSSTable(n):
    ascents = numAscentsLex(n)
    tvalues = tValues(n)
    columns = []
    for i in range(n):
        indices = findIndices(ascents, i)
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
    tvalues = tValues(n)
    columns = []
    for i in range(1, n + 1):
        indices = findIndices(sw, i)
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
    labels = [i for i in range(1, n + 1)]
    table = pd.DataFrame(columns)
    table = table.transpose()
    return table.rename(columns={i: labels[i] for i in range(n)})


def endsWithSSTable(n):
    ew = endsWithLex(n)
    tvalues = tValues(n)
    columns = []
    for i in range(1, n + 1):
        indices = findIndices(ew, i)
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
    labels = [i for i in range(1, n + 1)]
    table = pd.DataFrame(columns)
    table = table.transpose()
    return table.rename(columns={i: labels[i] for i in range(n)})