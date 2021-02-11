class Solution:
	def maskPII(self, S: str) -> str:
		if self.isEmail(S):
			return self.maskEmail(S)
		else:
			return self.maskPhoneNum(S)
	
	def isEmail(self, S: str) -> bool:
		for char in S:
			if char == "@":
				return True
		return False

	def maskEmail(self, S: str) -> str:
		atLoc = 0
		for i, char in enumerate(S):
			if char == "@":
				atLoc = i
		return S[0].lower() + "*****" + S[atLoc-1:].lower()

	def maskPhoneNum(self, S: str) -> str:
		possNums = set([str(i) for i in range(10)])
		regularizedNum = ""
		for char in S:
			if char in possNums:
				regularizedNum += char

		if len(regularizedNum) == 10:
			result = "***-***-"
		elif len(regularizedNum) == 11:
			result = "+*-***-***-"
		elif len(regularizedNum) == 12:
			result = "+**-***-***-"
		elif len(regularizedNum) == 13:
			result = "+***-***-***-"
		else:
			raise IllegalArgumentException("Check the phone number! Contact the developer if it's right.")

		return result + regularizedNum[len(regularizedNum)-4:]

