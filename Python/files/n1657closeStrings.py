from collections import Counter

class Solution:
	def closeStrings(self, word1: str, word2: str) -> bool:
		if len(word1) != len(word2):
			return False
			
		word1Dict = Counter(word1)
		word2Dict = Counter(word2)

		if sorted(list(word1Dict.keys())) != sorted(list(word2Dict.keys())):
			return False

		numCharInWord1 = [word1Dict[key] for key in word1Dict]
		numCharInWord2 = [word2Dict[key] for key in word2Dict]

		if sorted(numCharInWord1) != sorted(numCharInWord2):
			return False

		return True
