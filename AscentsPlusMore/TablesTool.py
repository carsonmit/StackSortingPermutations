from AscentsTables import ascentSSTable, startsWithSSTable, endsWithSSTable

'''These tables provide ways of partitioning permutations of S_n based on their behavior, one (likely more strong)
based on the number of ascents in a perm, and the other on the number the perm starts and ends with respectively. 
The functions are labeled accordingly and their only input is n, the desired size of S_n. Below the definition, 
you'll find functions whose input you can swap out for whatever you like.'''

# Modify the three lines below! All you need to do is change the input n to the size you want.
# Uncomment these for the various tables described above
'''ascentTable(4)
swTable(4)
ewTable(4) '''


# These just format the output
def ascentTable(n):
    print('''The columns are the number of ascents a given permutation in S_n has. These are the Eulerian numbers
    and the kth column will have A(n,k) total permutations. Furthermore, each of these A(n,k) are partitioned into n 
    rows depending on if they are 0, 1,..., or n-1 stack sortable.''')
    print('# of Ascents:')
    print(ascentSSTable(n))
    return None


def swTable(n):
    print('''The columns are the number a given permutation in S_n starts with. There are n!/n = (n-1)! of these
    permutations in each column. Furthermore, each of these (n-1)! are partitioned into n rows depending on if they are 
    0, 1,..., or n-1 stack sortable.''')
    print('Starting Number:')
    print(startsWithSSTable(n))
    return None


def ewTable(n):
    print('''The columns are the number a given permutation in S_n ends with. There are n!/n = (n-1)! of these
    permutations in each column. Furthermore, each of these (n-1)! are partitioned into n rows depending on if they are 
    0, 1,..., or n-1 stack sortable.''')
    print('Ending Number:')
    print(endsWithSSTable(n))
    return None