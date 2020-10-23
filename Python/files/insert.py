class Solution:
	def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
		l, r = 0,len(intervals)-1
		while l <= r:
			mid = int((l+r)/2)
			if intervals[mid][0] > newInterval[0]:
				r = mid-1
			else:
				l = mid+1

		indexToInsert = l
		if len(intervals) != 1:
			intervals.insert(indexToInsert, newInterval)
		else:
			if newInterval[0] > intervals[0][0]:
				intervals.append(newInterval)
			else:
				intervals.insert(0, newInterval)

		merged = [intervals[0].copy()]
		mergedIndex = 0
		for interval in intervals:
			if interval[0] <= merged[mergedIndex][1]:
				merged[mergedIndex][1] = max(interval[1], merged[mergedIndex][1])
			else:
				merged.append(interval)
				mergedIndex += 1
		return merged

		return intervals
