class Solution:
	def minCharacters(self, a: str, b: str) -> int:
		ab = self.checkCond1Or2(a, b)
		ba = self.checkCond1Or2(b, a)
		return min(ab, ba, self.checkCond3(a, b))
	
	def checkCond1Or2(self, s1: str, s2: str) -> int:
		s1NumChar = self.arrangeChar(s1)
		s2NumChar = self.arrangeChar(s2)
		numOPs1Lower = float('inf')
		numOPs2Lower = float('inf')

		# s1 is lower
		for i in range(1, 26):
			s1Info = self.findLeftRight(s1NumChar, i)
			s2Info = self.findLeftRight(s2NumChar, i)
			numOPs1Lower = min(s1Info[0]+s2Info[1], numOPs1Lower)

		return min(numOPs1Lower, numOPs2Lower)
		
	def checkCond3(self, a: str, b: str) -> int:
		return self.countNumChangesToUnify(a) + self.countNumChangesToUnify(b)

	def countNumChangesToUnify(self, s: str) -> int:
		charDict = {}
		dominantChar = 'a'
		numOfDominantChar = 0
		for char in s:
			if char not in charDict:
				charDict[char] = 1
			else:
				charDict[char] += 1
			numOfDominantChar += 1 if char == dominantChar else 0
			if numOfDominantChar < charDict[char]:
				dominantChar = char
				numOfDominantChar = charDict[char]
		return len(s) - numOfDominantChar

	def arrangeChar(self, s: str) -> [int]:
		numChars = [0] * 26
		aInNum = ord('a')
		for char in s:
			numChars[ord(char)-aInNum] += 1
		return numChars

	def findLeftRight(self, numChar: [int], index: int) -> [int, int]:
		return [sum(numChar[:index]), sum(numChar[index:])]
