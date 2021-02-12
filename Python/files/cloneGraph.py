from .basicClasses.Helper import Node
from queue import Queue
from collections import deque

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node == None:
            return None
        if not node.neighbors:
            return Node(val = 1)

        listOfNodes = deque()

        listOfNodes.append(node)
        visited = set()
        allNodes = {}

        while listOfNodes:
            nodeToCopy = listOfNodes.pop() # to make into bfs, use popleft()

            # Protection is needed because when node 2 and 4 is linked to 3, node 3 will be added twice if node 3 is not visited before.
            if nodeToCopy.val not in visited:
                visited.add(nodeToCopy.val)

                if nodeToCopy.val not in allNodes:
                    allNodes[nodeToCopy.val] = Node(val = nodeToCopy.val)

                for neighbour in nodeToCopy.neighbors:
                    if neighbour.val not in visited:
                        listOfNodes.append(neighbour)
                    if neighbour.val not in allNodes:
                        allNodes[neighbour.val] = Node(val = neighbour.val)
                    allNodes[nodeToCopy.val].neighbors.append(allNodes[neighbour.val])

        return allNodes[node.val]
