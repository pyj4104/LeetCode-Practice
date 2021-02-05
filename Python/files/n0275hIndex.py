class Solution:
	def hIndex(self, citations: [int]) -> int:
		if not citations:
			return 0
		if len(citations) == 1:
			if citations[0] == 0:
				return 0

		left = 0
		right = len(citations)-1
		backwardArr = [i+1 for i in range(len(citations))][::-1]
		ans = 0
		while left <= right:
			middle = int((left+right)/2)
			if len(citations[middle:]) <= citations[middle]:
				ans = len(citations[middle:])
				right = middle - 1
			else:
				left = middle + 1
		return ans
