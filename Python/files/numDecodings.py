class Solution:
	def numDecodings(self, s: str) -> int:
		if not s or s == "0":
			return 0

		retVal = [0] * (len(s)+1)
		retVal[0:2] = [1,1 if s[0] != "0" else 0]
		for i in range(2, len(s)+1):
			if int(s[i-1:i]) != 0:
				retVal[i] += retVal[i-1]
			if 10 <= int(s[i-2:i]) <= 26:
				retVal[i] += retVal[i-2]
			print(retVal)
		return retVal[-1]