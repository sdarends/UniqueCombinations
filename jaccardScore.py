
# given two lists, the method will calculate the similarity between the two
# two example lists are:
# listA = [['C', 2, 1], ['A', 4], ['B', 5, 3]]
# listB = [['B', 4, 1], ['C', 5, 2], ['A', 3]]

# jaccard divides the intersection of two sets by the union of two sets
def calculate():
    listA = [['C', 2, 1], ['A', 4], ['B', 5, 3]]
    listB = [['B', 4, 1], ['C', 5, 2], ['A', 3]]

    intersection = set(listA).intersection(set(listB))

    return intersection