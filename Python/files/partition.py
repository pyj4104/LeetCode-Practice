def makePartition(inStr: str):
	amoutOfLetters = {}

	for char in inStr:
		if char in amoutOfLetters:
			amoutOfLetters[char] += 1
		else:
			amoutOfLetters[char] = 1

	i = 0
	partition = []
	while i < len(inStr):
		partitionLength = __makePartition__(inStr[i:], amoutOfLetters, {})
		partition.append(partitionLength)
		i += partitionLength

	return partition

def __makePartition__(inStr: str, letterCount: {str: int}, letterKeep: {str: int}):
	# if depth more than 0 and letterKeep is 0, then return with the depth
	remaining = 0
	for key in letterKeep.keys():
		remaining += letterKeep[key]

	if letterKeep and remaining == 0:
		return 0

	if inStr[0] in letterKeep:
		letterKeep[inStr[0]] -= 1
	else:
		letterKeep[inStr[0]] = letterCount[inStr[0]] - 1

	return 1 + __makePartition__(inStr[1:], letterCount, letterKeep)

print(makePartition('abcadef'))
print(makePartition('abcadefed'))
print(makePartition('abcadefg'))
print(makePartition('a'))
