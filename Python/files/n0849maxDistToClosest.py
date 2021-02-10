class Solution:
	def maxDistToClosest(self, seats: [int]) -> int:
		num0s = []
		i = 0

		while seats[i] != 1:
			i += 1

		num0s.append(i)

		i += 1
		numSeatsInMid = 0

		while i < len(seats):
			if seats[i] == 1:
				num0s.append(numSeatsInMid)
				numSeatsInMid = 0
			else:
				numSeatsInMid += 1
			i += 1
		num0s.append(numSeatsInMid)

		if len(num0s) == 2:
			return max(num0s)
		else:
			maxDist = ((max(num0s[1:len(num0s)-1])+1) // 2)
			maxDist = max(num0s[0], maxDist, num0s[-1])

		return maxDist
