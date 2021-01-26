def qSort(arr: [int]) -> [int]:
	if len(arr) <= 1:
		return arr
	pivot = arr[0]
	lower = qSort([arr for arr in arr[1:] if arr < pivot])
	higher = qSort([arr for arr in arr[1:] if arr >= pivot])
	return lower + [pivot] + higher

class Solution:
    def carPooling(self, trips: [[int]], capacity: int) -> bool:
        distance = [0] * 1000
        for trip in trips:
        	distance[trip[1]] += trip[0]
        	distance[trip[2]] -= trip[0]
        pplInCar = 0
        for i in distance:
        	pplInCar += i
        	if pplInCar > capacity:
        		return False
        return True
