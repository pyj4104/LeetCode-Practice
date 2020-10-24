class Solution:
	def groupAnagrams(self, strs: [str]) -> [[str]]:
		numCharDictToAns = {}
		numChar = [[0 for i in range(26)] for j in range(len(strs))]
		for i, word in enumerate(strs):
			for char in word:
				numChar[i][ord(char)-ord('a')] += 1
			key = str(numChar[i])
			if key in numCharDictToAns:
				numCharDictToAns[key].append(word)
			else:
				numCharDictToAns[key] = []
				numCharDictToAns[key].append(word)
		retVal = []
		for group in numCharDictToAns.values():
			retVal.append(group)

		return retVal