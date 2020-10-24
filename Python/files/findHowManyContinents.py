
# [0, 1, 1, 0]
# [1, 1, 0, 0]
# [0, 0, 0, 0]
# [0, 1, 1, 0]


earth = [[0,1,1,0],
         [1,1,0,0],
         [0,0,0,0],
         [0,1,0,1]]

class Node:
    def __init__(self, isLand: bool, myCoordinate: (int, int)):
        self.isLand = isLand
        self.visited = False
        self.up = (myCoordinate[0], myCoordinate[1]-1)
        self.down = (myCoordinate[0], myCoordinate[1]+1)
        self.left = (myCoordinate[0]-1, myCoordinate[1])
        self.right = (myCoordinate[0]+1, myCoordinate[1])

class Solution:
    def findHowManyContinents(self, inVal = [int]) -> int:
        if len(inVal) == 0:
            return 0
        
        retVal = 0
        earthInNode = self.generateGraph(inVal)
        self.horiLength = len(inVal[0])
        for j, y in enumerate(earthInNode):
            for i, x in enumerate(y):
                # if it's land, check whether it had been visited
                if x.isLand and not x.visited:
                    retVal += 1
                    self.dfs(earthInNode, x)

        return retVal
    
    def generateGraph(self, earth = [[int]]) -> Node:
        earthCoordinate = []
        for j, y in enumerate(earth):
            xVal = []
            for i, x in enumerate(y):
                isLand = bool(earth[j][i])
                xVal.append(Node(isLand, (i, j)))
            earthCoordinate.append(xVal)
        return earthCoordinate
    
    def dfs(self, earthInNode: [[Node]], cur: Node):
        if not cur.isLand:
            return None
        if cur.visited:
            return None
        
        cur.visited = True
        up = earthInNode[cur.up[1]][cur.up[0]] if cur.up[1] > -1 else None
        left = earthInNode[cur.left[1]][cur.left[0]] if cur.left[0] > -1 else None
        
        if cur.down[1] <= len(earthInNode)-1:
            down = earthInNode[cur.down[1]][cur.down[0]]
        else:
            down = None
        
        if cur.right[0] <= self.horiLength-1:
            right = earthInNode[cur.right[1]][cur.right[0]]
        else:
            right = None

        if up:
            self.dfs(earthInNode, up)
        if left:
            self.dfs(earthInNode, left)
        if down:
            self.dfs(earthInNode, down)
        if right:
            self.dfs(earthInNode, right)
        
s = Solution()
testcases = [
    [[[0,1,1,0],
     [1,1,1,0],
     [0,0,0,1],
     [0,1,0,1]], 3],
    [[[1]], 1],
    [[[0,1,1,0],
     [1,1,0,0],
     [0,0,0,0],
     [0,1,0,1],
      [0,1,0,1]], 3]]

for tc in testcases:
    assert s.findHowManyContinents(tc[0]) == tc[1]
