from .basicClasses.Helper import Helper

class Solution:
    def findCircleNum(self, friendMatrix):
        if not friendMatrix:
            return 0

        numRepresentations = []
        for i, row in enumerate(friendMatrix):
            numRepresentation = 0
            for j, val in enumerate(row):
                numRepresentation += val * (2 ** j)
            numRepresentations.append(numRepresentation)
        
        for i, numRepresentationi in enumerate(numRepresentations):
            merged = False
            for j, friendRepresentationj in enumerate(numRepresentations[i+1:], start = i + 1):
                if numRepresentationi & friendRepresentationj:
                    merged = True
                    numRepresentations[j] = numRepresentationi|friendRepresentationj
            if merged:
                numRepresentations[i] = 0

        answer = 0
        for repre in numRepresentations:
            if repre:
                answer += 1

        return answer
