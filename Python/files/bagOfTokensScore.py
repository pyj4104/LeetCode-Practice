class Solution:
	def qSort(self, arr: []):
		if len(arr) <= 1:
			return arr
		pivot = arr[0]
		lower = self.qSort([num for num in arr[1:] if num < pivot])
		higher = self.qSort([num for num in arr[1:] if num >= pivot])
		return lower + [pivot] + higher

	def bagOfTokensScore(self, tokens: [int], P: int) -> int:
		if not tokens:
			return 0

		tokens.sort()
		sortedToken = tokens
		score = 0

		left = 0
		right = len(sortedToken) - 1

		if sortedToken[left] > P:
			return 0

		while left <= right:
			if left == right and P < sortedToken[left]:
				right -= 1
			else:
				if sortedToken[left] <= P:
					P -= sortedToken[left]
					left += 1
					score += 1
				else:
					P += sortedToken[right]
					right -= 1
					score -= 1

		return score


