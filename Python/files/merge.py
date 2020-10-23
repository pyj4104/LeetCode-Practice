class Solution:
	def qSortByFirst(self, intervals: [[int]]) -> [[int]]:
		if len(intervals) < 1:
			return intervals
		pivot = intervals[0]
		lower = self.qSortByFirst([interval for interval in intervals[1:] if interval[0] < pivot[0]])
		higher = self.qSortByFirst([interval for interval in intervals[1:] if interval[0] >= pivot[0]])
		return lower + [pivot] + higher

	def merge(self, intervals: [[int]]) -> [[int]]:
		if not intervals:
			return []
		intervals = self.qSortByFirst(intervals)
		merged = [intervals[0].copy()]
		mergedIndex = 0
		for interval in intervals:
			if interval[0] <= merged[mergedIndex][1]:
				merged[mergedIndex][1] = max(interval[1], merged[mergedIndex][1])
			else:
				merged.append(interval)
				mergedIndex += 1
		return merged
		