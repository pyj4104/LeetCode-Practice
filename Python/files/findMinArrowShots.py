from collections import deque

class Solution:
	def findMinArrowShots(self, points: [[int]]) -> int:
		if not points:
			return 0
		if len(points) == 1:
			return 1

		points.sort()
		retPoints = []
		before = points[0]
		for i in range(1, len(points)):
			after = points[i]
			overlap = self.doesOverlap(before, after)
			if not overlap:
				retPoints.append(before)
				before = after
			else:
				before = overlap
		retPoints.append(before)

		print(retPoints)
		return len(retPoints)

	def doesOverlap(self, point1: [int, int], point2: [int, int]) -> [int, int]:
		if point1[0] == point2[0]:
			if point1[1] > point2[1]:
				higher, lower = point1, point2
			else:
				lower, higher = point1, point2
		elif point1[0] <= point2[0]:
			lower, higher = point1, point2
		else:
			lower, higher = point2, point1

		if lower[1] >= higher[0]:
			return [higher[0], min(higher[1], lower[1])]
		else:
			return False
