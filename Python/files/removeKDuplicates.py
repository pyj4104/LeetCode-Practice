class Solution:
	def removeDuplicates(self, s: str, k: int) -> str:
		if not s or len(s) < k:
			return s

		stack = []

		for char in s:
			if self.checkK(stack, k-1, char):
				for i in range(k-1):
					stack.pop()
			else:
				stack.append(char)

		result = ""
		for char in stack:
			result += char

		return result

	def checkK(self, s: [], k: int, lastChar: str) -> bool:
		if len(s) < k:
			return False

		pos = len(s)-1

		for i in range(k):
			if lastChar != s[pos]:
				return False
			pos -= 1
		return True

	def removeDuplicatesEfficient(self, s: str, k: int) -> str:
		if not s or len(s) < k:
			return s

		stack = []

		for char in s:
			if not self.checkK(stack, k-1, char):
				stack.append((char, 1))

		result = ""
		for char, i in stack:
			for j in range(i):
				result += char

		return result

	def checkK(self, s: [], k: int, lastChar: str) -> bool:
		if not s:
			return False

		lastItem, count = s.pop()

		if lastItem == lastChar:
			if count == k:
				return True
			else:
				count += 1
				s.append((lastItem, count))
				return True
		else:
			s.append((lastItem, count))
			return False
