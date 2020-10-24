from math import ceil, floor

a = [1, 2, 4, 5, 6, 7, 8]
b = [1, 2, 3, 5, 6, 7, 8]
c = [1, 2, 3, 4, 5, 7, 8]
d = [1, 2, 3, 4, 5, 6, 8]
e = [1, 3]
f = [2, 3, 4, 5, 6, 8, 9]

def findMissingElement(arr):
	arrOri = arr
	while True:
		if len(arr) == 2:
			# Middle is missing
			if arr[0] + 1 != arr[1]:
				return arr[0] + 1
			else:
				arr0Index = arr[0]-arrOri[0]
				arr1Index = arr0Index + 1
				# Left is missing
				if arr[0] - 1 != arrOri[arr0Index]-1:
					return arr[0] - 1
				# Right is missing
				else:
					return arr[1] + 1

		# Grab min and max
		minElem = arr[0]
		maxElem = arr[len(arr)-1]
		midIndex = ceil(len(arr)/2)
		midNumInArr = arr[midIndex]

		# Find the ideal weight when all elements are in the array
		idealLeftWeight = midNumInArr - 1
		idealRightWeight = maxElem - midNumInArr + 1
		leftWeight = len(arr[:midIndex])
		rightWeight = len(arr[midIndex:])
		arrLeft = arr[:midIndex]
		arrRight = arr[midIndex:]

		# Cut the tree and move down
		if leftWeight < idealLeftWeight:
			arr = arrLeft
		elif rightWeight < idealRightWeight:
			arr = arrRight

print(findMissingElement(a))
assert findMissingElement(a) == 3
print(findMissingElement(b))
assert findMissingElement(b) == 4
print(findMissingElement(c))
assert findMissingElement(c) == 6
print(findMissingElement(d))
assert findMissingElement(d) == 7
print(findMissingElement(e))
print(findMissingElement(f))