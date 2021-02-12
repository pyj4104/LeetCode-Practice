class Solution:
	def restoreIpAddresses(self, s: str) -> [str]:
		if len(s) < 4 or len(s) > 12:
			return []
		return self.dfsStateless(s, "", 1)
		
	def dfsStateless(self, remainingS: int, addrSoFar: str, depth: int) -> [str]:
		ans = []
		if depth == 4:
			if self.checkValidityOfIP(addrSoFar+remainingS):
				ans.append(addrSoFar+remainingS)
		else:
			if remainingS:
				for i in range(3):
					digit = remainingS[:i+1]
					returnedVal = self.dfsStateless(remainingS[i+1:], addrSoFar+digit+".", depth + 1)
					if returnedVal:
						ans += returnedVal
		return ans
	
	def dfs(self, ans: [str], remainingS: int, addrSoFar: str, depth: int):
		if depth == 4:
			if self.checkValidityOfIP(addrSoFar+remainingS):
				ans.append(addrSoFar+remainingS)
		else:
			if remainingS:
				for i in range(3):
					digit = remainingS[:i+1]
					self.dfs(ans, remainingS[i+1:], addrSoFar+digit+".", depth + 1)

	def checkValidityOfIP(self, s: str):
		nums = s.split(".")
		if len(nums) != 4:
			return False
		for num in nums:
			if not num:
				return False
			if str(int(num)) != num:
				return False
			if int(num) > 255:
				return False
		return True
