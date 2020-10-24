class Solution:
	def fullJustify(self, words: [str], maxWidth: int) -> [str]:
		if not words:
			return ''

		i = 0
		groupings = []
		while i < len(words):
			grouping = [words[i]]
			numSpaces = maxWidth
			numSpaces -= len(words[i])
			totWordsLength = len(words[i])
			i += 1
			while i < len(words):
				if numSpaces-1 < len(words[i]):
					break
				numSpaces -= (len(words[i])+1)
				grouping.append(words[i])
				totWordsLength += len(words[i])
				i += 1
			groupings.append((grouping, totWordsLength))

		zerosInfo = []
		for grouping, totWordsLength in groupings:
			numSpaces = len(grouping)-1
			if numSpaces != 0:
				numSpacesBetweenBase = int((maxWidth-totWordsLength)/numSpaces)
				remainderOfSpaces = (maxWidth-totWordsLength)%numSpaces
				hasRemainder = remainderOfSpaces != 0
				zerosInfo.append([numSpacesBetweenBase, hasRemainder, remainderOfSpaces])
			else:
				zerosInfo.append([0, False, 0])

		i = 0
		retVal = []
		for grouping, totWordsLength in groupings[:len(groupings)-1]:
			line = grouping[0]
			numSpacesBetweenBase = zerosInfo[i][0]
			for j in range(1, len(grouping)):
				if zerosInfo[i][1] and (j-1) < zerosInfo[i][2]:
					precedingZeros = (' '*(numSpacesBetweenBase + 1))
					line += (precedingZeros+grouping[j])
				else:
					precedingZeros = (' '*(numSpacesBetweenBase))
					line += (precedingZeros + grouping[j])
			if len(grouping) == 1:
				tailingZeroNum = maxWidth-totWordsLength
				line += (' '*tailingZeroNum)
			retVal.append(line)
			i += 1

		grouping, totWordsLength = groupings[len(groupings)-1]

		line = grouping[0]
		for word in grouping[1:]:
			line += (' '+word)
		tailingZeroNum = maxWidth-totWordsLength
		tailingZeroNum -= 0 if len(grouping) == 0 else len(grouping)-1
		line += (' '*tailingZeroNum)
		retVal.append(line)

		return retVal
