class Solution:
	def canMakePaliQueries(self, s: str, queries: [[int]]) -> [bool]:
		isPoss = []
		sToDict = {}
		sInCharDict = []
		for char in s:
			if char in sToDict:
				sToDict[char] += 1
			else:
				sToDict[char] = 1
			sInCharDict.append(sToDict.copy())
		for query in queries:
			if query[0]-1 < 0:
				dictBefore = {}
			else:
				dictBefore = sInCharDict[query[0]-1]
			dictAfter = sInCharDict[query[1]].copy()
			for key in dictBefore:
				dictAfter[key] -= dictBefore[key]
			numReplacementsNeeded = 0
			for key in dictAfter:
				if dictAfter[key]%2 == 1:
					numReplacementsNeeded+=1
			numReplacementsNeeded = int(numReplacementsNeeded/2)
			if numReplacementsNeeded <= query[2]:
				isPoss.append(True)
			else:
				isPoss.append(False)
		return isPoss
