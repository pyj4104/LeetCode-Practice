from collections import deque

class Solution:
	def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
		if not popped:
			return True

		stack = deque()
		stack.append(pushed[0])
		poppedIndex = 0
		pushedIndex = 1

		while pushedIndex < len(pushed):
			peekedElem = stack[-1] if stack else None
			if peekedElem == popped[poppedIndex]:
				stack.pop()
				poppedIndex += 1
			else:
				stack.append(pushed[pushedIndex])
				pushedIndex += 1

		while stack:
			peekedElem = stack[-1]
			if peekedElem == popped[poppedIndex]:
				stack.pop()
				poppedIndex += 1
			else:
				return False

		return True
		