# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# Given an array with numbers, return the maximum number of consecutive items, and their contents
# e.g. [3, 99, 5, 101, 100, 99] => 3, [99, 100, 101]

# Sol 1. Sort and follow the numbers
# Sol 2.
    # Put it into a dictionary with the key as the element.
    # for each key,
        # Move up while connected
        # Move down while connected
            # Make sure to mark visited bool
class elem:
    def __init__(self, val: int):
        self.val = val
        self.up = val + 1
        self.down = val - 1
        self.visited = False

def findConsEasy(arr):
    arr.sort()
    
    prev = arr[0]
    startingNum = prev
    length = 1
    maxLength = 1
    maxStarting = 0
    i = 1
    
    for elem in arr[1:]:
        i += 1
        if elem == (prev + 1):
            length += 1
        elif elem == prev:
            pass
        else:
            length = 1
            startingNum = elem
        
        if maxLength < length:
            maxLength = length
            maxStarting = i
        prev = elem

    return (maxLength, arr[maxStarting-maxLength:maxStarting])

def findCon(arr):
    dictTree = {}
    for num in arr:
        dictTree[num] = elem(val = num)

    retVal = []

    for key in dictTree.keys():
        candidate = []
        if not dictTree[key].visited:
            __findCon__(dictTree, dictTree[key], candidate)
        if len(candidate) > len(retVal):
            retVal = candidate

    return (len(retVal), retVal)

# input: the dictionary, node, candidate
# output: list of the consequitive numbers
def __findCon__(dictTree: {int: elem}, node: elem, candidate: list):
    dictTree[node.val].visited = True
    candidate.append(node.val)
    if node.up in dictTree.keys() and not dictTree[node.up].visited:
        __findCon__(dictTree, dictTree[node.up], candidate)
    if node.down in dictTree.keys() and not dictTree[node.down].visited:
        __findCon__(dictTree, dictTree[node.down], candidate)

print(findConsEasy([3, 99, 5, 101, 100, 99]))
print(findCon([3, 99, 5, 101, 100, 99]))
print(findCon([100, 4, 200, 1, 3, 2]))
