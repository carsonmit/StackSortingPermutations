def findIndices(list, item):  # Given list and a particular item, outputs an array of all indices where item is in list
    x = -1  # Initializes x so it can start at 0 in the while statement
    indices = []
    while True:
        try: index = list.index(item, x + 1)  # Finds first index of item at or after the index x+1
        except ValueError: break
        else:
            indices.append(index)
            x = index
    return indices
