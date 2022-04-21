from AscentsTables import ascentSSTable,startsWithSSTable

'''These tables provide two ways of partitioning permutations of S_n based on their behavior, one (likely more strong)
based on the number of ascents in a perm and the other on the number the perm starts with. The two functions are labeled 
accordingly and their only input is n, the desired size of S_n. Below the definition, you'll find functions whose
 input you can swap out for whatever you like.'''


def ascentTable(n):
    print('''The columns represent the number of ascents a given permutation in S_n has. These are the Eulerian numbers
    and the kth column will contain A(n,k) total permutations. Furthermore, each of these A(n,k) are partitioned into n 
    rows depending on if they are 0, 1,..., or n-1 stack sortable.''')
    print('# of Ascents:')
    print(ascentSSTable(n))
    return None


def swTable(n):
    print('''The columns represent the number a given permutation in S_n starts with. There are n!/n = (n-1)! of these
    permutations in each column. Furthermore, each of these (n-1)! are partitioned into n rows depending on if they are 
    0, 1,..., or n-1 stack sortable.''')
    print('Starting Number:')
    print(startsWithSSTable(n))
    return None


'''Modify this code here! All you need to do is change the input n to the size you want.'''
'''The pattern among the ascents will likely be stronger than among the starting numbers, although its quite strange
how well-behaved their tables are relative to one another. We suspect there may be relationships between binomials or
potentially even fibonacci/ modular catalan numbers in some/most of the columns. There is also some nice symmetry
as you will see.'''
ascentTable(4)
swTable(4)