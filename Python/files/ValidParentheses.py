class Solution:
	def isValid(self, s: str) -> bool:
		if s == '':
			return True
		stack = []
		pair = {"]": "[", "}": "{", ")": "("}
		for char in s:
			if char not in pair:
				stack.append(char)
			else:
				if stack:
					if stack[len(stack)-1] == pair[char]:
						stack.pop()
					else:
						return False
				else:
					return False
		if stack:
			return False
		return True

s = Solution()
tcs = ["()",
'}',
'{(})',
'{[()]}']
for tc in tcs:
	print(s.isValid(tc))