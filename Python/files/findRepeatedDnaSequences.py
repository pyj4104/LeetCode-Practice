class Solution:
	def findRepeatedDnaSequences(self, s: str) -> [str]:
		if len(s) < 10:
			return []
			
		combs = {}
		for i in range(len(s)-10+1):
			curSeq = s[i:i+10]
			if curSeq in combs:
				combs[curSeq] += 1
			else:
				combs[curSeq] = 1

		retArr = []
		for key in combs:
			if combs[key] > 1:
				retArr.append(key)

		return retArr
