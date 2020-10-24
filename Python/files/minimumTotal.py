from .basicClasses.Helper import Helper

class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        lenOfLastRow = len(triangle[-1])
        triangle.append([0]*(lenOfLastRow+1))
        triangle = triangle[::-1]
        for rowNum in range(1, len(triangle)):
            Helper.PrintMatrix(triangle)
            for colNum in range(len(triangle[rowNum])):
                num = triangle[rowNum][colNum]
                triangle[rowNum][colNum] = num+min(triangle[rowNum-1][colNum], triangle[rowNum-1][colNum+1])
        return triangle[-1][0]